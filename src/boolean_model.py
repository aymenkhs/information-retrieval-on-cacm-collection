from nltk import word_tokenize

from src.document import Document

def boolean_model(query):
	relevent_documents = [document for document in Document.DOCUMENTS if rsv(query, document)]
	return relevent_documents

def rsv(query, document):
	return eval(query_processing(query, document))

def query_processing(query, document):
	query = word_tokenize(query)
	new_query = []
	for word in query:
		if word.lower() in ['and', 'or', 'not', '(', ')']:
			new_query.append(word)
		else:
			new_query.append(str(document.word_exist(word.lower())))

	return ' '.join(new_query)
