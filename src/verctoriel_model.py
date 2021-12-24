from nltk import word_tokenize

from src.document import Document
from src.tfidf import get_weight

def internal_product(query, document, inverse_weight_matrix):
	sum = 0
	for word in query:
		if word in inverse_weight_matrix:
			weight = get_weight(inverse_weight_matrix, document, word)
			if weight != None:
				sum += weight
	return sum

def rsv(query, document, inverse_weight_matrix, measure_function=internal_product):
	query = word_tokenize(query)
	query = [word.lower() for word in query if word not in Document.STOPWORDS]

	return measure_function(query, document, inverse_weight_matrix)

def vectorial_model(query, inverse_weight_matrix, measure_function=internal_product):
	print(query)
	for document in Document.DOCUMENTS:
		rsv(query, document, inverse_weight_matrix, measure_function)
