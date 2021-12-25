
class Request:

	REQUESTS = []

	def __init__(self, id, content, expected_results):

		self.id = id
		self.content = content
		self.expected_results = expected_results

	def __str__(self):
		return str(self.id)

	def __repr__(self):
		return str(self)
