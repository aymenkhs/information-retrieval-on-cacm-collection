import argparse

from src.tfidf import execute_tfidf
from src.pkl import load_results
from src.evaluations import launch_all_evaluations, evaluate_vectorial_function
from src.read_file import read_requests
from src.requests import Request
from ui.ui import launch_ui

from src.boolean_model import boolean_model


def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-e', '--evaluations', action='store_true', help='launch evaluations')
	parser.add_argument('-t', '--test', action='store_true', help='test function')
	return parser.parse_args()

def main():
	args = parse_arguments()

	if args.evaluations:
		read_requests()
		inverse_weight_matrix, inverse_structure = load_results()
		launch_all_evaluations(inverse_weight_matrix)
	elif args.test:
		inverse_weight_matrix, inverse_structure = load_results()
		svd = boolean_model('Algebraic')
		import pdb; pdb.set_trace()

	else:
		launch_ui()




if __name__ == '__main__':
	main()
