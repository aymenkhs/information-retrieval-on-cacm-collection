import numpy as np
import pandas as pd

from src.vectorial_model import vectorial_model, LIST_MEASURES_FUNCTIONS
from src.requests import Request
from src.read_file import read_requests

calculate_fmeasure = lambda p, r : (2 * p * r) / (p + r)
calculate_precision = lambda docs_pert_select, docs_select : docs_pert_select / docs_select
calculate_recall = lambda docs_pert_select, docs_pert : docs_pert_select / docs_pert


def evaluate(selected_documents, request):
	 docs_pert_select = [document for document in selected_documents if document.id in request.expected_results]
	 recall = calculate_precision(len(docs_pert_select), len(request.expected_results))
	 precision = calculate_precision(len(docs_pert_select), len(selected_documents))
	 return precision, recall

def evaluate_vectorial_function(inverse_weight_matrix, function):
	read_requests()
	tresholds = [x/10 for x in list(range(1,10))]
	evaluations_results = pd.DataFrame(columns=['request', 'treshold', 'precision', 'recall', 'fmeasure'])
	for request in Request.REQUESTS:
		if len(request.expected_results) == 0:
			continue

		for treshold in tresholds:
			selected_documents = vectorial_model(request.content,
				inverse_weight_matrix, LIST_MEASURES_FUNCTIONS[function])
			print(y-x)
			if len(selected_documents) == 0:
				break

			precision, recall = evaluate(selected_documents, request)
			if precision == 0 and recall == 0:
				fmeasure = 0
			else:
				fmeasure = calculate_fmeasure(precision, recall)

			print(request.id, treshold, precision, recall, fmeasure)
			df2 = [request.id, treshold, precision, recall, fmeasure]
			evaluations_results.append(df2, ignore_index = True)

	import pdb; pdb.set_trace()
