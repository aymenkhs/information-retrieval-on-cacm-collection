import math

from nltk import word_tokenize

from src.document import Document

def internal_product(query, document, inverse_weight_matrix):
	sum = 0
	for word in document.words:
		if word in query:
			sum += inverse_weight_matrix[word][document.id]
	return sum

def dice_coeficient(query, document, inverse_weight_matrix):
	product, power2, cmpt = loop_caluculation(query, document, inverse_weight_matrix)
	if product == 0:
		return 0
	return (2 * product) / (power2 + cmpt)

def cosinus_measure(query, document, inverse_weight_matrix):
	product, power2, cmpt = loop_caluculation(query, document, inverse_weight_matrix)
	if product == 0:
		return 0
	return product / math.sqrt(power2 * cmpt)

def jaccard_measure(query, document, inverse_weight_matrix):
	product, power2, cmpt = loop_caluculation(query, document, inverse_weight_matrix)
	if product == 0:
		return 0
	return product / (power2 + cmpt - product)

def loop_caluculation(query, document, inverse_weight_matrix):
	product = 0
	power2 = 0
	cmpt = 0
	for word in document.words:
		if word in query:
			product += inverse_weight_matrix[word][document.id]
			cmpt+=1
		power2 += (inverse_weight_matrix[word][document.id] ** 2)
	return product, power2, cmpt

def rsv(query, document, inverse_weight_matrix, measure_function=internal_product):
	return measure_function(query, document, inverse_weight_matrix)

def vectorial_model(query, inverse_weight_matrix, measure_function=internal_product, threshold=0.1):
	query = word_tokenize(query)
	query = [word.lower() for word in query if word not in Document.STOPWORDS]
	
	relevent_documents = []
	for document in Document.DOCUMENTS:
		result = rsv(query, document, inverse_weight_matrix, measure_function)
		if result >= threshold:
			relevent_documents.append(document)
	return relevent_documents

LIST_MEASURES_FUNCTIONS = {
	'internal product' : internal_product,
	'dice coeficient' : dice_coeficient,
	'cosinus measure' : cosinus_measure,
	'jaccard measure' : jaccard_measure,
}
