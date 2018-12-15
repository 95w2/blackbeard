import tkinter as tk
from PIL import ImageTk, Image
import os, csv

with open("save.csv", 'r') as file:
	entryValues = list(csv.reader(file))[1]

class Main(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)

		self.master = master
		master.title("logger")
		master.resizable(0, 0)

		self.topbar = tk.Menu(master)
		dropdown = tk.Menu(master)
		dropdown.add_command(label="Undo", command=lambda: self.undo())
		dropdown.add_command(label="Reset", command=lambda: self.reset())
		self.topbar.add_cascade(label="Actions", menu=dropdown)
		self.topbar.add_command(label="New Session", command=lambda: self.new())
		master.config(menu=self.topbar)

		self.image = Image.open("assets/logo.png")
		self.image.thumbnail((300, 300), Image.ANTIALIAS)
		self.img = ImageTk.PhotoImage(self.image)
		self.panel = tk.Label(self.master, image=self.img)
		self.panel.grid(row=0, rowspan=4, column=0, sticky="nesw")

		self.total = 0
		self.totalLabel = tk.Label(self.master, font=("Arial", 24), width=20)
		self.totalLabel.grid(row=0, column=1, columnspan=2, pady=40, sticky="nesw")

		self.neidanImg = ImageTk.PhotoImage(file="assets/neidan.png")
		self.neidan = tk.Label(self.master, image=self.neidanImg)
		self.shellImg = ImageTk.PhotoImage(file="assets/shell.png")
		self.shell = tk.Label(self.master, image=self.shellImg)
		self.steelImg = ImageTk.PhotoImage(file="assets/steel.png")
		self.steel = tk.Label(self.master, image=self.steelImg)

		self.neidan.grid(row=1, column=1, sticky="e")
		self.shell.grid(row=2, column=1, sticky="e")
		self.steel.grid(row=3, column=1, pady=(0, 20), sticky="e")

		vcmd = self.master.register(self.validate)
		self.entry1 = tk.Entry(self.master, width=10, validate="key", vcmd=(vcmd, '%P'))
		self.entry2 = tk.Entry(self.master, width=10)
		self.entry3 = tk.Entry(self.master, width=10)
		
		self.temp = None
		self.entries = [self.entry1, self.entry2, self.entry3]
		for i in range(0, 3):
			self.entries[i].insert(0, entryValues[i])
			self.entries[i].config(state="readonly")
			self.entries[i].bind('<Return>', lambda event: self.focus_set())
		self.update("Total")

		self.entry1.grid(row=1, column=2, padx=(10, 30), sticky="w")
		self.entry2.grid(row=2, column=2, padx=(10, 30), sticky="w")
		self.entry3.grid(row=3, column=2, padx=(10, 30), pady=(0, 20), sticky="w")

		self.bind('<Button-1>', lambda event: self.focus_set())
		self.grid(row=0, rowspan=4, column=0, columnspan=4, padx=3, pady=3, sticky="nesw")	

	def validate(self, value):
		try:
			x = int(value)
			return True
		except:
			return False

	def update(self, mode):
		entrySum = int(self.entry1.get())*100000 + int(self.entry2.get())*409200 + int(self.entry3.get())*100000000
		self.total = "{:,}".format(entrySum)
		self.totalLabel['text'] = f"{mode}:  ${self.total}"

	def new(self):
		self.totalLabel['text'] = f"Session:  $0"

		for entry in self.entries:
			entry.config(state="normal")
			entry.insert(0, 0)
			entry.bind('<FocusOut>', lambda event: self.update("Session"))

		self.topbar.delete("New Session")
		self.topbar.add_command(label="End Session", command=lambda: self.end())
		self.topbar.add_command(label="Cancel")

	def end(self):
		self.temp = entryValues
		self.totalLabel['text'] = f"Total:  ${self.total}"

		for i in range(0, 3):
			entryValues[i] += self.entries[i].get()
			self.entries[i].insert(0, entryValues[i])
			self.entries[i].config(state="readonly")
			self.entries[i].unbind('<FocusOut>')

		self.topbar.delete("End Session")
		self.topbar.delete("Cancel")
		self.topbar.add_command(label="New Session", command=lambda: self.new())

	def undo(self):
		if self.temp:
			entryValues = self.temp
		self.update("Total")

	def reset(self):
		entryValues = [0]*3
		for entry in self.entries:
			entry.insert(0, 0)
		self.update("Total")

root = tk.Tk()
main = Main(root)
root.mainloop()

with open("save.csv", 'w') as file:
	csv_writer = csv.writer(file)
	csv_writer.writerow(["neidan", "shell", "steel shell"])
	csv_writer.writerow(entryValues)



