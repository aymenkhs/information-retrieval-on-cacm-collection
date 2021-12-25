import os

import pandas as pd

from src.vectorial_model import vectorial_model, LIST_MEASURES_FUNCTIONS
from src.requests import Request

RESULT_FOLDER = 'evaluation_results'

calculate_fmeasure = lambda p, r : (2 * p * r) / (p + r)
calculate_precision = lambda docs_pert_select, docs_select : docs_pert_select / docs_select
calculate_recall = lambda docs_pert_select, docs_pert : docs_pert_select / docs_pert

MEASURES_THRESHOLDS = {
	'internal product': (0, 35, 5, 10),
	'dice coeficient': (0, 50, 5, 100),
	'cosinus measure': (0, 6, 1, 10),
	'jaccard measure': (0, 50, 5, 100),
}

class EvaluationError(Exception):
	def __init__(self):
		self.message = 'There are no expected documents for this query'

	def __str__(self):
		return self.message

def evaluate(selected_documents, request):
	 docs_pert_select = [document for document in selected_documents if document.id in request.expected_results]
	 recall = calculate_precision(len(docs_pert_select), len(request.expected_results))
	 precision = calculate_precision(len(docs_pert_select), len(selected_documents))
	 return precision, recall

def evaluate_vectorial_function(inverse_weight_matrix, function, request, treshold):

	if len(request.expected_results) == 0:
		raise EvaluationError()
	selected_documents = vectorial_model(request.content,
		inverse_weight_matrix, LIST_MEASURES_FUNCTIONS[function], threshold=treshold)
	if len(selected_documents) == 0:
		precision, recall, fmeasure = 0, 0, 0
	else :
		precision, recall = evaluate(selected_documents, request)
		if precision == 0 and recall == 0:
			fmeasure = 0
		else:
			fmeasure = calculate_fmeasure(precision, recall)
	return precision, recall, fmeasure, selected_documents

def evaluate_and_store(inverse_weight_matrix, function, tresholds=(1, 10, 1, 10)):
	start, end, step, div = tresholds
	tresholds = [x/div for x in list(range(start+step, end, step))]

	list_results = []
	for request in Request.REQUESTS:
		if len(request.expected_results) == 0:
			continue

		for treshold in tresholds:
			selected_documents = vectorial_model(request.content,
				inverse_weight_matrix, LIST_MEASURES_FUNCTIONS[function], threshold=treshold)
			if len(selected_documents) == 0:
				precision, recall, fmeasure = 0, 0, 0
			else :
				precision, recall = evaluate(selected_documents, request)
				if precision == 0 and recall == 0:
					fmeasure = 0
				else:
					fmeasure = calculate_fmeasure(precision, recall)

			print(request.id, treshold, precision, recall, fmeasure)
			df2 = [request.id, treshold, precision, recall, fmeasure]
			list_results.append(df2)
	evaluations_results = pd.DataFrame(list_results, columns=['request', 'treshold', 'precision', 'recall', 'fmeasure'])
	evaluations_results.to_csv(os.path.join(RESULT_FOLDER, '{}.csv'.format(function)))

def launch_all_evaluations(inverse_weight_matrix):
	for function in LIST_MEASURES_FUNCTIONS:
		evaluate_and_store(inverse_weight_matrix, function, tresholds=MEASURES_THRESHOLDS[function])
