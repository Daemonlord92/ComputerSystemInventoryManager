from tkinter import *

class InventoryManager(object):
	"""docstring for InventoryManager"""
	def __init__(self, master):
		self.master = master
		master.title = ("Invenger")


root = Tk()
my_gui = InventoryManager(root)
root.mainloop()
