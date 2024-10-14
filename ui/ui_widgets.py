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
        input_label = ttk.Label(self.frame, text="Input signals:")

        sig_A= ttk.Button(self.frame,text="Signal A", command=lambda: self.loadSignal('A'),bootstyle=SUCCESS)
        sig_B= ttk.Button(self.frame,text="Signal B",command=lambda: self.loadSignal('B'),bootstyle=SUCCESS)
        save_output=ttk.Button(self.frame,text="Save Output Signal",command=lambda: self.saveOutput(filename_entry.get()),bootstyle=(SUCCESS,OUTLINE))
        clear_output=ttk.Button(self.frame,text="Clear Output",command=self.clearOutput,bootstyle=(SUCCESS,OUTLINE))

        filename_label = ttk.Label(self.frame, text="Save file name:")
        self.save_file = StringVar()
        filename_entry = ttk.Entry(self.frame, textvariable=self.save_file)
        self.frame.grid(column=0, row=0,sticky=(W, E))
        input_label.grid(column=0, row=1,sticky=(W, E))
        sig_A.grid(column=0, row=2,columnspan=2,sticky=(W, E))
        sig_B.grid(column=2, row=2,columnspan=2,sticky=(W, E))
        self.fig_in, self.ax_in, self.canvas_in = self.initialize_graph('Input Signal(s)','t','x(t)')
        self.fig_out,self.ax_out, self.canvas_out = self.initialize_graph('Output Signal','t','x(t)')

        self.canvas_in.get_tk_widget().grid(column=0, row=0,columnspan=4)
        self.canvas_out.get_tk_widget().grid(column=4, row=0,columnspan=4)
        filename_label.grid(column=4, row=1,sticky=(W, E))
        filename_entry.grid(column=5, row=1, columnspan=3, sticky=(W, E))
        save_output.grid(column=4,row=2,columnspan=4, sticky=(N, W, E, S))
        clear_output.grid(column=4,row=3,columnspan=4, sticky=(N, W, E, S))

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
        if sig=='A':
            self.A=Signal(x,y)
            self.plot_graph(self.ax_in,self.canvas_in,self.A,'Input Signal(s)');       
        elif sig=='B':
            self.B=Signal(x,y)     
            self.plot_graph(self.ax_in,self.canvas_in,self.B,'Input Signal(s)');       
    
    
    def saveOutput(self, file):
        if self.Out == None:
            show_message_box("DSP" , "No output signal to save")
        elif not file :
            show_message_box("DSP" , "Please enter save file name")
        else:
            print(self.Out.x)
            print(self.Out.y)

            output=np.stack((self.Out.x,self.Out.y),axis=1)
            np.savetxt(fname=file+'.txt',header=str(len(self.Out.x)), comments='', fmt='%i', delimiter=' ', X=output)
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

    def plot_graph(self,ax,canvas,signal,title):
        ax.set_title(title)
        ax.plot(signal.x, signal.y, marker='o'),
        canvas.draw()
