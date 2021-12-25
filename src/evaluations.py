import numpy as np
import pandas as pd

from src.vectorial_model import vectorial_model, LIST_MEASURES_FUNCTIONS
from src.requests import Request
from src.read_file import read_requests

def fmeasure(precision, recall):
	pass

def precision():
	pass

def recall():
	pass

def evaluate(selected_documents, request):
	pass




def evaluate_vectorial_function(function, tresholds_param):
	read_requests()
	import pdb; pdb.set_trace()
	treshold_min, treshold_max, treshold_step = tresholds_param
	evaluations_results = pd.DataFrame(columns=np.arange(treshold_min, treshold_max, treshold_step))
	for request in Request.REQUESTS:
		for treshold in np.arange(treshold_min, treshold_max, treshold_step):
			print(vectorial_model(request.content, inverse_weight_matrix, LIST_MEASURES_FUNCTIONS[function]))
