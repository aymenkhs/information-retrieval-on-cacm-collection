import os
import re

from src.document import Document

FILE_PATH = os.path.join("cacm", "cacm.all")

def read_file(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

def read_docs(content):

	documents = []

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

		documents.append(Document(id_doc, title, abstract))

	return documents
