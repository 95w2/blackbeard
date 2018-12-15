import tkinter as tk
from PIL import ImageTk, Image
import os, csv

print("hello")
'''
with open("test.csv", 'w') as file:
	csv_writer = csv.writer(file)
	csv_writer.writerow([1])
'''

class Main(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)

		self.master = master
		master.title("logger")
		master.resizable(0, 0)

		self.topbar = tk.Menu(master)
		self.topbar.add_command(label="New Session", command=lambda: self.master.register(self.new()))

		master.config(menu=self.topbar)

		self.image = Image.open("logo.png")
		self.image.thumbnail((300, 300), Image.ANTIALIAS)
		self.img = ImageTk.PhotoImage(self.image)
		self.panel = tk.Label(self.master, image=self.img)
		self.panel.grid(row=0, rowspan=4, column=0, sticky="nesw")

		self.session = 0
		self.total = 0

		self.totalLabel = tk.Label(self.master, text=f"Total:  ${self.total}", font=("Arial", 24), width=20)
		self.totalLabel.grid(row=0, column=1, columnspan=2, pady=40, sticky="nesw")

		self.neidanimg = ImageTk.PhotoImage(file="neidan.png")
		self.neidan = tk.Label(self.master, image=self.neidanimg)
		self.neidan.grid(row=1, column=1, sticky="e")

		self.shellimg = ImageTk.PhotoImage(file="shell.png")
		self.shell = tk.Label(self.master, image=self.shellimg)
		self.shell.grid(row=2, column=1, sticky="e")

		self.steelimg = ImageTk.PhotoImage(file="steel.png")
		self.steel = tk.Label(self.master, image=self.steelimg)
		self.steel.grid(row=3, column=1, pady=(0, 20), sticky="e")

		self.entry1 = tk.Entry(self.master, width=10)
		self.entry2 = tk.Entry(self.master, width=10)
		self.entry3 = tk.Entry(self.master, width=10)

		self.entry1.grid(row=1, column=2, padx=(10, 30), sticky="w")
		self.entry2.grid(row=2, column=2, padx=(10, 30), sticky="w")
		self.entry3.grid(row=3, column=2, padx=(10, 30), pady=(0, 20), sticky="w")

		self.grid(row=0, rowspan=4, column=0, columnspan=4, padx=3, pady=3, sticky="nesw")
		#self.latest = tk.Label(self.master, width=50, text="Latest Run:")
		#self.latest.grid(row=1, column=1, sticky="nesw")

	def new(self):

		self.totalLabel['text'] = f"Session:  ${self.session}"

		self.entry1.config(state="disabled")
		self.entry2.config(state="disabled")
		self.entry3.config(state="disabled")

		self.topbar.delete("New Session")
		self.topbar.add_command(label="End Session", command=lambda: print("ok"))


root = tk.Tk()
main = Main(root)
root.mainloop()