from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class UI:
    def initialize(self):
        root = Tk()
        root.title("Digital Signal Processing")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        notebook = ttk.Notebook(root)
        notebook.grid(column=0, row=0, sticky=(N, W, E, S))  # Use grid for notebook
        return root, notebook

class Tab:
    def __init__(self,notebook,name):
        self.notebook=notebook
        self.name=name
        self.frame = ttk.Frame(notebook,padding="3 3 12 12")
        sig_A= ttk.Button(self.frame,text="Signal A")
        sig_B= ttk.Button(self.frame,text="Signal B")
        fig = plt.Figure(figsize=(4, 3), dpi=100)
        ax = fig.add_subplot(111)
        canvas =  FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        display=ttk.Button(self.frame,text="Display Signal")

        self.frame.grid(column=0, row=0,sticky=(W, E))
        sig_A.grid(column=0, row=0,columnspan=2,sticky=(W, E))
        sig_B.grid(column=2, row=0,columnspan=2,sticky=(W, E))
        canvas.get_tk_widget().grid(column=0, row=3,columnspan=4)

        display.grid(column=0,row=4,columnspan=4, sticky=(N, W, E, S))
       
    def add(self):
        for child in self.frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        self.notebook.add(self.frame, text=self.name)
