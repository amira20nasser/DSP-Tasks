from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import os
from tkinter import messagebox
from numpy import loadtxt

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
            sig_A= ttk.Button(self.frame,text="Signal A", command=lambda: self.loadSignal('A'))
            sig_B= ttk.Button(self.frame,text="Signal B",command=lambda: self.loadSignal('B'))
            display=ttk.Button(self.frame,text="Display Signal",command=self.displaySignal)

            self.frame.grid(column=0, row=0,sticky=(W, E))
            sig_A.grid(column=0, row=0,columnspan=2,sticky=(W, E))
            sig_B.grid(column=2, row=0,columnspan=2,sticky=(W, E))
            self.ax_in, self.canvas_in = self.initialize_graph()

            self.canvas_in.get_tk_widget().grid(column=0, row=3,columnspan=4)

            display.grid(column=0,row=4,columnspan=4, sticky=(N, W, E, S))
        
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
              self.Ax,self.Ay=x,y
              self.plot_graph(self.ax_in,self.canvas_in,self.Ax,self.Ay);       
            elif sig=='B':
                self.Bx,self.By=x,y     
                self.plot_graph(self.ax_in,self.canvas_in,self.Bx,self.By);       
     
        
        def displaySignal(self, file):
            print("display_signal Logic")
                #return signal 

        def initialize_graph(self):
        
            fig, ax = plt.subplots(figsize=(5, 5))
            # ax.set_title('Signal')
            # ax.set_xlabel('Indices')
            # ax.set_ylabel('Samples')
            canvas = FigureCanvasTkAgg(fig, master=self.frame)
            # canvas_widget.pack( fill='both', expand=True)
            return ax,canvas

        def plot_graph(self,ax,canvas,indices,samples):
            ax.plot(indices, samples, marker='o')
            canvas.draw()