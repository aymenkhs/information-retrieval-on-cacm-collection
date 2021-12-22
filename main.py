from src.read_file import *
from src.document import Document

def main():
	Document.STOPWORDS = read_stop_list()
	documents = read_docs(read_file(DOCUMENT_FILE_PATH))
	for document in documents:
		document.tokenise()
	import pdb; pdb.set_trace()

if __name__ == '__main__':
	main()
