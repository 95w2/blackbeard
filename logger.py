import tkinter as tk
from PIL import ImageTk, Image
import os, csv

print("hello")
'''
with open("test.csv", 'w') as file:
	csv_writer = csv.writer(file)
	csv_writer.writerow([1])
'''

class New(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)

		'''
		self.image = Image.open("logo.png")
		self.image.thumbnail((500,300), Image.ANTIALIAS)
		self.img = ImageTk.PhotoImage(self.image)
		self.panel = tk.Label(self, image=self.img)
		self.panel.grid(row=0, rowspan=4, column=0, sticky="nesw")
		
		self.label = tk.Label(self, width=50, text="Total:")
		self.label.grid(row=0, column=0, sticky="nesw")
		'''


class Main(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)

		self.master = master
		master.title("logger")
		#self['bg'] = "#3d2d21"
		'''
		master.resizable(0, 0)
		menubar = tk.Menu(master)
		menubar.add_command(label="Hello!")
		menubar.add_command(label="Quit!")
		master.config(menu=menubar)
		'''

		self.image = Image.open("logo.png")
		self.image.thumbnail((300, 300), Image.ANTIALIAS)
		self.img = ImageTk.PhotoImage(self.image)
		self.panel = tk.Label(self.master, image=self.img)
		self.panel.grid(row=0, rowspan=4, column=0, sticky="nesw")

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
		self.new = New(self.master)
		self.button.grid_forget()
		self.button2.grid_forget()
		self.button3.grid_forget()
		self.button4.grid_forget()
		self.new.grid(row=0, rowspan=4, column=1, sticky="nesw")

root = tk.Tk()
main = Main(root)

# create a toplevel menu
menubar = tk.Menu(root)
filemenu = tk.Menu(root)
filemenu.add_command(label="Hello!", command=lambda: print("hello"))
menubar.add_cascade(label="Quit!", menu=filemenu)

# display the menu
root.config(menu=menubar)
root.mainloop()