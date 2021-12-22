from src.read_file import *

def main():
	documents = read_docs(read_file(FILE_PATH))
	for document in documents:
		document.tokenise()
	import pdb; pdb.set_trace()

if __name__ == '__main__':
	main()
