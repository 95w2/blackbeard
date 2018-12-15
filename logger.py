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

		self.image = (Image.open("logo.png"))
		self.image.thumbnail((500,300), Image.ANTIALIAS)
		self.img = ImageTk.PhotoImage(self.image)
		self.panel = tk.Label(self.master, image=self.img)
		self.panel.grid(row=0, column=0, sticky="nesw")

root = tk.Tk()
main = Main(root)
root.mainloop()