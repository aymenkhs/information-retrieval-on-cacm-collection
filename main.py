from src.tfidf import indexation, inverse_file, tf_idf
from src.boolean_model import boolean_model
from src.verctoriel_model import vectorial_model

def main():
	indexation()
	inverse_structure = inverse_file()
	inverse_weight_matrix = tf_idf(inverse_structure)
	vectorial_model('preliminary or not algebraic and boat', inverse_weight_matrix)

if __name__ == '__main__':
	main()
