from src.tfidf import indexation, inverse_file, tf_idf
from src.boolean_model import boolean_model

def main():
	indexation()
	inverse_structure = inverse_file()
	inverse_weight_matrix = tf_idf(inverse_structure)
	relevent_documents = boolean_model('preliminary or not algebraic and boat')
	print(relevent_documents)

if __name__ == '__main__':
	main()
