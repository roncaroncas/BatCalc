import csv

class Bateria():

	def __init__(self):

		self.cTab = cTable()
		self.pTab = pTable()

		self.infos = {
			'nome': "",
			'fabricante': "",
			'vnom': 12,
			'cell_num'
			'peso': 0,
			'res_interna'
			'dimensoes': {"L": 0, "A": 0, "P": 0},
			'terminal': ""
		}



class Table():

	def __init__(self):
		self.rowHeader = []
		self.colHeader = []
		self.content = []

	def __getitem__(self,key):
		return self.content[k]

	def __str__(self):
		
		s = "\n---Descarga a {}---\n".format(self.kind)

		#HEADER - AUTONOMIA
		s += "\t"
		for i in range(len(self.rowHeader)):
			s += "{}min\t".format(int(self.rowHeader[i]))
		s+="\n"

		for i in range(len(self.colHeader)):
			s += "{:4.2f}V\t".format(self.colHeader[i])

			for j in range(len(self.rowHeader)):
				s += "{:7.2f}\t".format(self.content[i][j])
			s += "\n"

		return s

	def importCSV(self, filename):

		self.__init__()

		with open(filename, newline='') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
			self.rowHeader = next(spamreader)[1:]
			for row in spamreader:
				self.colHeader.append(row[0])
				self.content.append(row[1:])

		for i in range(len(self.rowHeader)):
			self.rowHeader[i] = float(self.rowHeader[i].replace(",",".")) 

		for i in range(len(self.colHeader)):
			self.colHeader[i] = float(self.colHeader[i].replace(",",".")) 

		for i in range(len(self.content)):
			for j in range(len(self.content[i])):
				self.content[i][j] =  float(str(self.content[i][j]).replace(",",".")) 
			
		print(self)


class pTable(Table):
	kind = "Potência Constante"

class cTable(Table):
	kind = "Corrente Constante"