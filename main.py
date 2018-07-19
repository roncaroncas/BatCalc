from model import Bateria, pTable, cTable
import views
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# from tkinter.filedialog import askopenfilename, asksaveasfilename

class Controller(Tk):
	def __init__(self):
		Tk.__init__(self)
		self._frame = None
		#self.switch_frame(views.PageMenu)
		self.switch_frame(views.PageNewBattery)
		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)

	def switch_frame(self, frame_class):
		new_frame = frame_class(self)
		if self._frame is not None:
			self._frame.destroy()
		self._frame = new_frame

		self._frame.grid(row=0, column=0, sticky="NSEW")

		if (self._frame.__class__.__name__ == "PageNewBattery"):
			self._frame.import_p_button.config(command=lambda:self.createTable("p"))
			self._frame.import_c_button.config(command=lambda:self.createTable("c"))



	def createTable(self, kind):

		filename = filedialog.askopenfilename()

		if kind == "p":
			tab = pTable()
			table_frame = self._frame.pTable_frame
			f = self._frame.frame3

		if kind == "c":
			tab = cTable()
			table_frame = self._frame.cTable_frame
			f = self._frame.frame4

		tab.importCSV(filename)

		#Clear cTableFrame
		table_frame.destroy()
		table_frame = ttk.Frame(f)

		#Recriando Tabela		
		for j in range(len(tab.rowHeader)): #AutHeader
			b = ttk.Label(table_frame, text="{:.0f} min".format(tab.rowHeader[j]), relief="solid", borderwidth=2)
			b.grid(row=0, column=j+1, sticky="NSEW")

		for i in range(len(tab.colHeader)):
			#VeodHeader
			b = ttk.Label(table_frame, text="{:4.2f} V".format(tab.colHeader[i]), relief="solid", borderwidth=2)
			b.grid(row=i+1, column=0, sticky="NSEW")
			for j in range(len(tab.rowHeader)): #Columns
				b = ttk.Label(table_frame, text="{:5.2f}".format(tab.content[i][j]), relief="solid", borderwidth=2, width=9)
				b.grid(row=i+1, column=j+1, sticky="NSEW")

		table_frame.grid(row=1, column=0, sticky="NSEW")

		for child in table_frame.winfo_children():
			child.grid_configure(padx=2, pady=2)

root = Controller()
root.title("Cálculo de Baterias")

root.mainloop()



# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0,row=0,sticky=(N, W, E, S))
# mainframe.columnconfigure(0, weight=1)
# mainframe.rowconfigure(0, weight=1)

# feet=StringVar()
# meters=StringVar()
# feet_entry=ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W,E))
# meters_label = ttk.Label(mainframe, textvariable=meters)
# meters_label.grid(column=2, row=2, sticky=(W,E))
# button_calc = ttk.Button(mainframe, text="Calculate", command=calculate)
# button_calc.grid(column=3, row=3, sticky=(W))

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children(): 
# 	child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind('<Return>', calculate)


# class App(Tk):
# 	def __init__(self):
# 		Tk.__init__(self)
# 		self._frame = None
# 		self.switch_frame(views.StartPage)

# 	def switch_frame(self, frame_class):
# 		"""Destroys current frame and replaces it with a new one."""
# 		new_frame = frame_class(self)
# 		if self._frame is not None:
# 			self._frame.destroy()
# 		self._frame = new_frame
# 		self._frame.pack()


# if __name__ == "__main__":
# 	app = App()
# 	app.mainloop()

	# def print_csv(self):
	# 	filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
	# 	b.cTab.importCSV(filename)


b = Bateria()


#filename = asksaveasfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)