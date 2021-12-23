from src.read_file import *
from src.document import Document

def indexation():
	Document.STOPWORDS = read_stop_list()
	read_docs(read_file(DOCUMENT_FILE_PATH))
	for document in Document.DOCUMENTS:
		document.tokenise()
	return Document.DOCUMENTS

def inverse_file():
	words = Document.all_words()
	inverse_structure = {}
	for word in words:
		inverse_structure[word] = []
		for document in Document.DOCUMENTS:
			if word in document.words:
				inverse_structure[word].append((document, document.frequency[word]))
	return inverse_structure

def main():
	indexation()
	inverse_structure = inverse_file()
	import pdb; pdb.set_trace()

if __name__ == '__main__':
	main()
