from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import os
from tkinter import messagebox
from numpy import loadtxt
from logic.basic_signal_operations import Signal

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
        self.A=None
        self.B=None
        self.Out=None
        sig_A= ttk.Button(self.frame,text="Signal A", command=lambda: self.loadSignal('A'))
        sig_B= ttk.Button(self.frame,text="Signal B",command=lambda: self.loadSignal('B'))
        save_output=ttk.Button(self.frame,text="Save Output Signal",command=self.saveOutput)

        self.frame.grid(column=0, row=0,sticky=(W, E))
        sig_A.grid(column=0, row=1,columnspan=2,sticky=(W, E))
        sig_B.grid(column=2, row=1,columnspan=2,sticky=(W, E))
        self.ax_in, self.canvas_in = self.initialize_graph('Input Signals','t','x(t)')
        self.ax_out, self.canvas_out = self.initialize_graph('Output Signals','t','x(t)')

        self.canvas_in.get_tk_widget().grid(column=0, row=0,columnspan=4)
        self.canvas_out.get_tk_widget().grid(column=4, row=0,columnspan=4)
        save_output.grid(column=4,row=1,columnspan=4, sticky=(N, W, E, S))
    
    def add(self):
        
        for child in self.frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        self.notebook.add(self.frame, text=self.name)

    def loadSignal(self,sig):
        file=filedialog.askopenfilename(initialdir = os.path.expanduser('~/Downloads'),
                                            title = "Select a text file containing the signal B.",
                                            filetypes = (("Text files","*.txt"),
                                                        ("all files",
                                                        "*.*")))
        x,y = loadtxt(file, dtype=int, skiprows=2, delimiter=" ", unpack=True)
        if sig=='A':
            self.A=Signal(x,y)
            self.plot_graph(self.ax_in,self.canvas_in,self.A);       
        elif sig=='B':
            self.B=Signal(x,y)     
            self.plot_graph(self.ax_in,self.canvas_in,self.B);       
    
    
    def saveOutput(self, file):
        print("display_signal Logic")
            #return signal 

    def initialize_graph(self,title,xlabel,ylabel):
    
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        # canvas_widget.pack( fill='both', expand=True)
        return ax,canvas

    def plot_graph(self,ax,canvas,signal):
        ax.plot(signal.x, signal.y, marker='o')
        canvas.draw()
