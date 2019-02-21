import csv

class Tab2CSVPlugin:
	def input(self, filename):
		self.myfile = filename

	def run(self):
		self.input_tabfile = csv.reader(open(self.myfile, "r"), delimiter = '\t')


	def output(self, filename):
		out_csvfile = csv.writer(open(filename, "w"))
		out_csvfile.writerows(self.input_tabfile)