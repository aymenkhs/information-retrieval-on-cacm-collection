from src.tfidf import indexation, inverse_file, tf_idf
from src.boolean_model import boolean_model
from src.vectorial_model import vectorial_model, LIST_MEASURES_FUNCTIONS
from src.pkl import save_results, load_results
from src.evaluations import evaluate_vectorial_function

def execute_tfidf():
	indexation()
	inverse_structure = inverse_file()
	inverse_weight_matrix = tf_idf(inverse_structure)
	save_results(inverse_weight_matrix, inverse_structure)
	return inverse_weight_matrix, inverse_structure

def main():
	inverse_weight_matrix, inverse_structure = load_results()
	evaluate_vectorial_function(inverse_weight_matrix, 'cosinus measure')

if __name__ == '__main__':
	main()
