import math

from src.read_file import *
from src.document import Document
from src.pkl import save_results

def indexation():
	Document.STOPWORDS = read_stop_list()
	read_docs(read_file(DOCUMENT_FILE_PATH))
	for document in Document.DOCUMENTS:
		document.tokenise()
	return Document.DOCUMENTS

def inverse_file():
	words = Document.all_words()
	inverse_structure = {}
	for document in Document.DOCUMENTS:
		for word in document.words:
			if word not in inverse_structure:
				inverse_structure[word] = {}
			inverse_structure[word][document] = document.frequency[word]
	return inverse_structure

def tf_idf(inverse_structure):
	weight = lambda ti, dj: (dj.frequency[ti]/dj.max_frequency()) * math.log10(Document.nb_documents()/len(inverse_structure[ti]) + 1)

	inverse_weight_matrix = {}
	for document in Document.DOCUMENTS:
		for word in document.words:
			if word not in inverse_weight_matrix:
				inverse_weight_matrix[word] = {}
			inverse_weight_matrix[word][document.id] = weight(word, document)
	return inverse_weight_matrix

def execute_tfidf():
	indexation()
	inverse_structure = inverse_file()
	inverse_weight_matrix = tf_idf(inverse_structure)
	save_results(inverse_weight_matrix, inverse_structure)
	return inverse_weight_matrix, inverse_structure
