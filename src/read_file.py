import os
import re

from src.document import Document
from src.requests import Request

DOCUMENT_FILE_PATH = os.path.join("cacm", "cacm.all")
STOPWORDS_FILE_PATH = os.path.join("cacm", "common_words")
QUERY_FILE_PATH = os.path.join("cacm", "query.text")
QRELS_FILE_PATH = os.path.join("cacm", "qrels.text")

def read_file(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

def read_docs(content):

	parts = re.split(r'\.I ', content)
	del parts[0]

	for part in parts:

		id_doc = re.search(r'^([0-9]*)\n', part).group(1)

		splits = re.split(r'\.W\n', part)

		if len(splits) == 1:
			m = re.search(r'\.T\n(.*)\n\.B\n', part, re.S)
		else:
			m = re.search(r'\.T\n(.*)\.W\n', part, re.S)
		try:
			title = m.group(1)
		except AttributeError as e:
			import pdb; pdb.set_trace()


		abstract = re.search(r'\.W\n(.*)\n\.B', part, re.S)

		if abstract is None:
			abstract = ''
		else:
			abstract = abstract.group(1)

		Document.DOCUMENTS.append(Document(id_doc, title, abstract))

	return Document.DOCUMENTS

def read_stop_list(file_path=STOPWORDS_FILE_PATH):
	content = read_file(file_path)
	words = content.split('\n')
	return words[:-1]

def read_requests(query_file_path=QUERY_FILE_PATH, qrels_file_path=QRELS_FILE_PATH):
	qrels = read_file(QRELS_FILE_PATH)
	qrels = qrels.split('\n')
	del qrels[-1]
	expected_results = {}
	for expected_result in qrels:
		expected_result = expected_result.split(' ')
		id = str(int(expected_result[0]))
		doc = expected_result[1]
		if id not in expected_results:
			expected_results[id] = [doc]
		else:
			expected_results[id].append(doc)

	requests = read_file(query_file_path)
	parts = re.split(r'\.I ', requests)
	del parts[0]

	for part in parts:
		id = re.search(r'^([0-9]*)\n', part).group(1)
		splits = re.split(r'\.A\n', part)
		if len(splits) == 1:
			m = re.search(r'\.W\n(.*)\n\.N\n', part, re.S)
		else:
			m = re.search(r'\.W\n(.*)\.A\n', part, re.S)
		request_content = m.group(1)
		if id in expected_results:
			Request.REQUESTS.append(Request(id, request_content, expected_results[id]))
		else:
			Request.REQUESTS.append(Request(id, request_content, []))

	return Request.REQUESTS
