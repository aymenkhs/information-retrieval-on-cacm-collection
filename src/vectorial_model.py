import math

from nltk import word_tokenize

from src.document import Document

def internal_product(query, document, inverse_weight_matrix):
	sum = 0
	for word in query:
		if word in inverse_weight_matrix:
			word_weight = inverse_weight_matrix[word]
			if document.id in word_weight:
				sum += word_weight[document.id]
	return sum

def dice_coeficient(query, document, inverse_weight_matrix):
	product = internal_product(query, document, inverse_weight_matrix)
	sum_power = sum_power_2(document, inverse_weight_matrix)
	return (2 * product) / (sum_power + len(query))

def cosinus_measure(query, document, inverse_weight_matrix):
	product = internal_product(query, document, inverse_weight_matrix)
	sum_power = sum_power_2(document, inverse_weight_matrix)
	return product / math.sqrt(sum_power * len(query))

def jaccard_measure(query, document, inverse_weight_matrix):
	product = internal_product(query, document, inverse_weight_matrix)
	sum_power = sum_power_2(document, inverse_weight_matrix)
	return product / (sum_power + len(query) - product)

def sum_power_2(document, inverse_weight_matrix):
	sum = 0
	for word in document.words:
		weight = inverse_weight_matrix[word][document.id]
		sum += (weight ** 2)
	return sum

def rsv(query, document, inverse_weight_matrix, measure_function=internal_product):
	query = word_tokenize(query)
	query = [word.lower() for word in query if word not in Document.STOPWORDS]

	return measure_function(query, document, inverse_weight_matrix)

def vectorial_model(query, inverse_weight_matrix, measure_function=internal_product, threshold=0.1):
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
