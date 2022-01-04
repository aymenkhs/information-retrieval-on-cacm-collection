import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from ui.main_interface import Ui_MainWindow

from src.pkl import load_results
from src.read_file import read_requests
from src.requests import Request
from src.evaluations import evaluate_vectorial_function

from src.tfidf import execute_tfidf
from src.boolean_model import boolean_model
from src.vectorial_model import vectorial_model, LIST_MEASURES_FUNCTIONS


TRANSLATION_MEASURES_FUNCTIONS = {
	'Produit Interne' : 'internal product',
	'Coeficient de Dice' : 'dice coeficient',
	'Mesure de Cosinus' : 'cosinus measure',
	'Mesure de Jaccard' : 'jaccard measure',
}

class Window(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)

		self.setWindowTitle('Projet RI')

		self.setup_values()
		self.setup_conections()

	def setup_values(self):
		read_requests()
		try:
			self.inverse_weight_matrix, self.inverse_structure = load_results()
		except FileNotFoundError as e:
			self.inverse_weight_matrix, self.inverse_structure = execute_tfidf()

		self.QueryText.setPlainText(Request.REQUESTS[0].content)

	def setup_conections(self):
		self.SearchInput.clicked.connect(self.search_by_input)
		self.SearchQueryText.clicked.connect(self.search_by_query)
		self.QueryNumber.valueChanged.connect(self.update_predifined_query)

	def search_by_query(self):
		if self.ModelChoice.currentText() == 'Le Model Boolean':
			QMessageBox.about(self, "Model Error",
			"This function isn't available for this model, please select the vectorial model in order to continue")
		else:
			# call the vectoriel model
			query_number = self.QueryNumber.value()
			threshold = self.Threshold.value()
			choice = self.MeasureChoice.currentText()
			precision, recall, fmeasure, selected_documents = evaluate_vectorial_function(
				self.inverse_weight_matrix, TRANSLATION_MEASURES_FUNCTIONS[choice],
							Request.REQUESTS[query_number-1], threshold)

			if not self.is_selection_empty(selected_documents):
				# show the content inside the list
				self.update_list(selected_documents)

			self.Precision.setText(str("%.5f" % precision))
			self.Recall.setText(str("%.5f" % recall))
			self.FMeasure.setText(str("%.5f" % fmeasure))

	def search_by_input(self):
		query = self.QueryInput.toPlainText()
		if query == "":
			QMessageBox.about(self, "the query must not be empty",
			"please write your query before clicking the search button")
			return

		if self.ModelChoice.currentText() == 'Le Model Boolean':
			# call the boolean model
			selected_documents = boolean_model(query)
		else:
			# call the vectoriel model
			threshold = self.Threshold.value()
			choice = self.MeasureChoice.currentText()
			selected_documents = vectorial_model(query, self.inverse_weight_matrix,
				measure_function=LIST_MEASURES_FUNCTIONS[TRANSLATION_MEASURES_FUNCTIONS[choice]],
										threshold=threshold)


		if not self.is_selection_empty(selected_documents):
			# show the content inside the list
			self.update_list(selected_documents)

	def is_selection_empty(self, selected_documents):
		if len(selected_documents) == 0:
			QMessageBox.about(self, "no document found",
			"No document has been found with this query and parameters")
			self.Result.clear()
			return True
		return False

	def update_list(self, selected_documents):
		# clear the list
		self.Result.clear()
		# add items
		for document in selected_documents:
			self.Result.addItem(document.id)

	def update_predifined_query(self, value):
		self.QueryText.setPlainText(Request.REQUESTS[value-1].content)

def launch_ui():
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	launch_ui()
