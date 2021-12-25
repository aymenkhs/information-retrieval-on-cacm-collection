import argparse

from src.tfidf import execute_tfidf
from src.boolean_model import boolean_model
from src.vectorial_model import vectorial_model, LIST_MEASURES_FUNCTIONS
from src.pkl import load_results
from src.evaluations import launch_all_evaluations
from src.read_file import read_requests


def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-e', '--evaluations', action='store_true', help='launch evaluations')
	parser.add_argument('-t', '--test', action='store_true', help='test function')
	return parser.parse_args()

def init():
	read_requests()
	inverse_weight_matrix, inverse_structure = load_results()
	return inverse_weight_matrix, inverse_structure

def main():
	args = parse_arguments()

	inverse_weight_matrix, inverse_structure = init()

	if args.evaluations:
		launch_all_evaluations(inverse_weight_matrix)
	elif args.test:
		pass
	else:
		pass
		# launch the UI




if __name__ == '__main__':
	main()
