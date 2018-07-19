import tkinter as tk
from tkinter import ttk

# class StartPage(tk.Frame):
# 	def __init__(self, master):
# 		tk.Frame.__init__(self, master)

# 		start_label = tk.Label(self, text="Cálculo de Baterias")
# 		page_1_button = tk.Button(self, text="1. Baterias",
# 								  command=lambda: master.switch_frame(PageBaterias))
# 		page_2_button = tk.Button(self, text="2. Configurações",
# 								  command=lambda: master.switch_frame(PageTwo))

# 		start_label.pack(side="top", fill="x", pady=10)
# 		page_1_button.pack()
# 		page_2_button.pack()

 
# class PageBaterias(tk.Frame):
# 	def __init__(self, master):
# 		tk.Frame.__init__(self, master)

# 		page_1_label = tk.Label(self, text="1. Baterias")

# 		new_battery_button = tk.Button(self, text="Criar Bateria",
# 								 command=lambda: master.switch_frame(PageNewBattery))

# 		start_button = tk.Button(self, text="Return to start page",
# 								 command=lambda: master.switch_frame(StartPage))
# 		page_1_label.pack(side="top", fill="x", pady=10)
# 		start_button.pack()
# 		new_battery_button.pack()

class PageNewBattery(tk.Frame):
	def __init__(self, master):

		def updateCB():
			val_celulas_checkbutton['text'] = val_celulas_var.get()

		ttk.Frame.__init__(self, master)

		titulo_label = ttk.Label(self, text="Bateria", anchor=tk.CENTER, borderwidth=2, relief="groove")
		titulo_label.grid(row=0, column=0, columnspan=2, sticky="NSEW")
		
		notebook = ttk.Notebook(self)
		notebook.grid(row=1, column=0,columnspan=2, sticky="NSEW")

		self.frame1 = ttk.Frame(notebook)
		self.frame2 = ttk.Frame(notebook)
		self.frame3 = ttk.Frame(notebook)
		self.frame4 = ttk.Frame(notebook)

		notebook.add(self.frame1, text="General Info")
		notebook.add(self.frame2, text="Mechanical Info")
		notebook.add(self.frame3, text="Potência")
		notebook.add(self.frame4, text="Corrente")

		save_button = ttk.Button(self, text="Salvar")
		cancel_button = ttk.Button(self, text="Cancelar")

		cancel_button.grid(row=2, column=0, sticky="NSEW")
		save_button.grid(row=2, column=1, sticky="NSEW")

		for child in self.winfo_children():
			child.grid_configure(padx=5, pady=5)

		#FRAME1
		f = self.frame1

		nome_label = ttk.Label(f, text="Nome:")
		nome_var = tk.StringVar()
		nome_entry = ttk.Entry(f, textvariable=nome_var)

		fabricante_label = ttk.Label(f, text="Fabricante:")
		fabricante_var = tk.StringVar()
		fabricante_entry = ttk.Entry(f, textvariable=fabricante_var)

		vnom_label = ttk.Label(f, text="Vnom:")
		vnom_var = tk.StringVar()
		vnom_combobox = ttk.Combobox(f, textvariable=vnom_var, values=["2V", "6V", "12V"])

		cell_num_label = ttk.Label(f, text="N. Células:")
		cell_num_var = tk.StringVar()
		cell_num_entry = ttk.Entry(f, textvariable=cell_num_var)

		peso_label = ttk.Label(f, text="Peso:")
		peso_var = tk.StringVar()
		peso_entry = ttk.Entry(f, textvariable=peso_var)

		res_interna_label = ttk.Label(f, text="Resistência Interna:")
		res_interna_var = tk.StringVar()
		res_interna_entry = ttk.Entry(f, textvariable=res_interna_var)

		nome_label.grid(row=0, column=0, sticky="NSEW")
		nome_entry.grid(row=0, column=1, sticky="NSEW")
		fabricante_label.grid(row=1, column=0, sticky="NSEW")
		fabricante_entry.grid(row=1, column=1, sticky="NSEW")
		vnom_label.grid(row=2, column=0, sticky="NSEW")
		vnom_combobox.grid(row=2, column=1, sticky="NSEW")
		cell_num_label.grid(row=3,column=0, sticky="NSEW")
		cell_num_entry.grid(row=3,column=1, sticky="NSEW")
		peso_label.grid(row=4,column=0, sticky="NSEW")
		peso_entry.grid(row=4,column=1, sticky="NSEW")
		res_interna_label.grid(row=5,column=0, sticky="NSEW")
		res_interna_entry.grid(row=5,column=1, sticky="NSEW")

		for child in f.winfo_children():
			child.grid_configure(padx=2, pady=2)

		f['padding'] = (10)
		f['borderwidth'] = 10
		f['relief'] = "solid"		

		#FRAME 2

		f = self.frame2

		imagem_label = ttk.Label(f, text="[IMAGEM]", borderwidth=2, relief="groove")

		terminal_label = ttk.Label(f, text="Terminal:")
		terminal_var = tk.StringVar()
		terminal_entry = ttk.Entry(f, textvariable=terminal_var)

		largura_label = ttk.Label(f, text="Largura:")
		largura_var = tk.StringVar()
		largura_entry = ttk.Entry(f, textvariable=largura_var)

		altura_label = ttk.Label(f, text="Altura:")
		altura_var = tk.StringVar()
		altura_entry = ttk.Entry(f, textvariable=altura_var)

		profundidade_label = ttk.Label(f, text="Profundida:")
		profundidade_var = tk.StringVar()
		profundidade_entry = ttk.Entry(f, textvariable=profundidade_var)


		imagem_label.grid(row=0,column=0, rowspan=4, sticky="NSEW")
		terminal_label.grid(row=0, column=1, sticky="NSEW")
		terminal_entry.grid(row=0, column=2, sticky="NSEW")
		largura_label.grid(row=1, column=1, sticky="NSEW")
		largura_entry.grid(row=1, column=2, sticky="NSEW")
		altura_label.grid(row=2, column=1, sticky="NSEW")
		altura_entry.grid(row=2, column=2, sticky="NSEW")
		profundidade_label.grid(row=3, column=1, sticky="NSEW")
		profundidade_entry.grid(row=3, column=2, sticky="NSEW")

		for child in f.winfo_children():
			child.grid_configure(padx=2, pady=2)

		f['padding'] = (10)
		f['borderwidth'] = 10
		f['relief'] = "solid"


		#FRAME 3

		f = self.frame3

		descricao_label = ttk.Label(f, text="DESCRIÇÃO... LOREM IPSUM")

		self.pTable_frame = ttk.Frame(f)

		val_celulas_var = tk.StringVar()
		val_celulas_var.set('Valores/Bateria')

		val_celulas_checkbutton = ttk.Checkbutton(f, text=val_celulas_var.get(), variable=val_celulas_var,
			onvalue='Valores/Células', offvalue='Valores/Bateria', command=updateCB)

		self.import_p_button = ttk.Button(f, text="Importar Tabela Potência")

		descricao_label.grid(row=0,column=0, sticky="NSEW")
		self.pTable_frame.grid(row=1, column=0, sticky="NSEW")
		val_celulas_checkbutton.grid(row=2, column=0, sticky="NSEW")
		self.import_p_button.grid(row=3, column=0, sticky="NSEW")


		for child in f.winfo_children():
			child.grid_configure(padx=2, pady=2)

		f['padding'] = (10)
		f['borderwidth'] = 10
		f['relief'] = "solid"


		#FRAME 4

		f = self.frame4

		descricao_label = ttk.Label(f, text="DESCRIÇÃO... LOREM IPSUM")

		self.cTable_frame = ttk.Frame(f)

		# cAutHeader = ['10min', '20min', '30min'] 
		# cVeodHeader = ['1,6V', '1,7V', '1,8V', '1,9V']
		# cContent = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

		# cNumRows = len(cVeodHeader)
		# cNumCols = len(cAutHeader)
		
		# for j in range(cNumCols): #AutHeader
		# 	b = ttk.Label(cTable_frame, text=cAutHeader[j], relief="solid", borderwidth=2)
		# 	b.grid(row=0, column=j+1, sticky="NSEW")

		# for i in range(cNumRows):
		# 	#VeodHeader
		# 	b = ttk.Label(cTable_frame, text=cVeodHeader[i], relief="solid", borderwidth=2)
		# 	b.grid(row=i+1, column=0, sticky="NSEW")
		# 	for j in range(cNumCols): #Columns
		# 		b = ttk.Label(cTable_frame, text=cContent[i][j], relief="solid", borderwidth=2)
		# 		b.grid(row=i+1, column=j+1, sticky="NSEW")

		self.import_c_button = ttk.Button(f, text="Importar Tabela Corrente")

		descricao_label.grid(row=0,column=0, sticky="NSEW")
		self.cTable_frame.grid(row=1, column=0, sticky="NSEW")
		self.import_c_button.grid(row=3, column=0, sticky="NSEW")

		for child in f.winfo_children():
			child.grid_configure(padx=2, pady=2)

		f['padding'] = (10)
		f['borderwidth'] = 10
		f['relief'] = "solid"



# class PageTwo(tk.Frame):
# 	def __init__(self, master):
# 		tk.Frame.__init__(self, master)

# 		page_2_label = tk.Label(self, text="2. Configurações")
# 		start_button = tk.Button(self, text="Return to start page",
# 								 command=lambda: master.switch_frame(StartPage))
# 		page_2_label.pack(side="top", fill="x", pady=10)
# 		start_button.pack()
