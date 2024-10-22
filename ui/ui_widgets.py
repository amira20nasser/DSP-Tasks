from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import os
from tkinter import messagebox
import numpy as np
from logic.basic_signal_operations import Signal
from utils import show_message_box

class UI:
    def initialize(self):
        root = ttk.Window(themename='flatly')

        # Configure the style for all widgets
        root.title("Digital Signal Processing")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        notebook = ttk.Notebook(root,padding=5,bootstyle=SECONDARY)
        notebook.grid(column=0, row=0, sticky=(N, W, E, S))  # Use grid for notebook
        return root, notebook

class Tab:

    def __init__(self,notebook,name):
        matplotlib.style.use('seaborn-v0_8-pastel')

        self.notebook=notebook
        self.name=name
        self.frame = ttk.Frame(notebook,padding="3 3 12 12")
        self.A=None
        self.B=None
        self.Out=None
        
    def add(self):
        for child in self.frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        self.notebook.add(self.frame, text=self.name)

    def loadSignal(self,sig,ax,canvas):
        
        file=filedialog.askopenfilename(initialdir = os.path.expanduser( os.getcwd()),title = "Select a text file containing the signal B.",filetypes = (("Text files","*.txt"), ("all files","*.*")))
        x,y = np.loadtxt(file, dtype=float, skiprows=3, delimiter=" ", unpack=True)
        setattr(self,sig,Signal(x,y))
        self.plot_discrete_graph(ax,canvas,getattr(self,sig),'Input Signal(s)');       

    

    def saveOutput(self, signal, file):
        if signal == None:
            show_message_box("DSP" , "No output signal to save")
        elif not file :
            show_message_box("DSP" , "Please enter save file name")
        else:
            print(signal.x)
            print(signal.y)
            output=np.stack((signal.x,signal.y),axis=1)
            np.savetxt(fname=file+'.txt',header=str(len(signal.x)), comments='', fmt='%i', delimiter=' ', X=output)
            show_message_box("DSP" , "Signal saved successfully")

    def clearOutput(self):
        self.Out=None
        self.ax_out.clear()
        self.ax_out.set_title('Output Signal')
        self.ax_out.set_xlabel('t')
        self.ax_out.set_ylabel('x(t)')
        self.canvas_out.draw()

    def initialize_graph(self,title,xlabel,ylabel):
        fig = plt.Figure(figsize=(5, 4))
        ax = fig.add_subplot(111)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        # canvas_widget.pack( fill='both', expand=True)
        return fig,ax,canvas

    def plot_discrete_graph(self,ax,canvas,signal,title):
        line_colors = ['b-', 'r-', 'g-','m-']
        ax.set_title(title)
        ax.stem(signal.x, signal.y, linefmt=line_colors[np.random.randint(4)],markerfmt="o" , basefmt="k"),
        canvas.draw()