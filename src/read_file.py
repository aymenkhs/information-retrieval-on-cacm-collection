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
		m = re.search(r'([0-9]*)\n\.T\n(.*)(\.W\n(.*)\n)?', part, re.S)

		id_doc = m.group(1)
		title = m.group(2)
		abstract = m.group(4)

		if abstract is None:
			abstract = ''

		if id_doc == '20':
			import pdb; pdb.set_trace()

		documents.append(Document(id_doc, title, abstract))

	import pdb; pdb.set_trace()
