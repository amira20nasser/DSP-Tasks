from tkinter import *
from tkinter import ttk
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
        save_output=ttk.Button(self.frame,text="Save Output Signal",command=lambda: self.saveOutput('output.txt'))

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
        file=filedialog.askopenfilename(initialdir = os.path.expanduser( os.getcwd()),
                                            title = "Select a text file containing the signal B.",
                                            filetypes = (("Text files","*.txt"),
                                                        ("all files",
                                                        "*.*")))
        x,y = np.loadtxt(file, dtype=int, skiprows=3, delimiter=" ", unpack=True)
        print("AFTER UPLOAD X",x) # x is numpy array 
        print("AFTER UPLOAD Y",y)
        if sig=='A':
            self.A=Signal(x,y)
            self.plot_graph(self.ax_in,self.canvas_in,self.A);       
        elif sig=='B':
            self.B=Signal(x,y)     
            self.plot_graph(self.ax_in,self.canvas_in,self.B);       
    
    
    def saveOutput(self, file):
        if self.Out == None:
            show_message_box("title" , "No output signal to save")
        else:
            print(self.Out.x)
            print(self.Out.y)

            output=np.stack((self.Out.x,self.Out.y),axis=1)
            np.savetxt(fname=file,header=str(len(self.Out.x)), delimiter=' ', X=output)


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
