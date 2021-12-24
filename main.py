from src.tfidf import indexation, inverse_file, tf_idf

def main():
	indexation()
	inverse_structure = inverse_file()
	inverse_weight_matrix = tf_idf(inverse_structure)
	import pdb; pdb.set_trace()

if __name__ == '__main__':
	main()
