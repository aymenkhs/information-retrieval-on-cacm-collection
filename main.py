from src.tfidf import indexation, inverse_file, tf_idf
from src.boolean_model import boolean_model
from src.vectorial_model import vectorial_model, LIST_MEASURES_FUNCTIONS
from src.pkl import save_results, load_results

def execute_tfidf():
	indexation()
	inverse_structure = inverse_file()
	inverse_weight_matrix = tf_idf(inverse_structure)
	save_results(inverse_weight_matrix, inverse_structure)
	return inverse_weight_matrix, inverse_structure

def main():
	inverse_weight_matrix, inverse_structure = load_results()
	string = 'What articles exist which deal with TSS (Time Sharing System), an \n operating system for IBM computers?'
	print(vectorial_model(string, inverse_weight_matrix, LIST_MEASURES_FUNCTIONS['cosinus measure']))

if __name__ == '__main__':
	main()
