import os
import pickle

from src.document import Document
from src.read_file import read_stop_list

PATH_RESULTS = 'saved_structures'

def save_results(inverse_weight_matrix, inverse_structure, path=PATH_RESULTS):
	path_documents = os.path.join(path, 'documents.pkl')
	path_inverse_weight_matrix = os.path.join(path, 'weight_matrix.pkl')
	path_inverse_structure = os.path.join(path, 'inverse_structure.pkl')

	with open(path_documents, 'wb') as file:
		my_pickler = pickle.Pickler(file)
		my_pickler.dump(Document.DOCUMENTS)

	with open(path_inverse_weight_matrix, 'wb') as file:
		my_pickler = pickle.Pickler(file)
		my_pickler.dump(inverse_weight_matrix)

	with open(path_inverse_structure, 'wb') as file:
		my_pickler = pickle.Pickler(file)
		my_pickler.dump(inverse_structure)

def load_results(path=PATH_RESULTS):
	path_documents = os.path.join(path, 'documents.pkl')
	path_inverse_weight_matrix = os.path.join(path, 'weight_matrix.pkl')
	path_inverse_structure = os.path.join(path, 'inverse_structure.pkl')

	with open(path_documents, 'rb') as file:
		my_unpickler = pickle.Unpickler(file)
		Document.DOCUMENTS = my_unpickler.load()

	with open(path_inverse_weight_matrix, 'rb') as file:
		my_unpickler = pickle.Unpickler(file)
		inverse_weight_matrix = my_unpickler.load()

	with open(path_inverse_structure, 'rb') as file:
		my_unpickler = pickle.Unpickler(file)
		inverse_structure = my_unpickler.load()

	Document.STOPWORDS = read_stop_list()

	return inverse_weight_matrix, inverse_structure
