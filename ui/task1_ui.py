from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from ui.ui_widgets import Tab  
from utils import *
from logic.basic_signal_operations import Signal
class Task1UI(Tab):
    def __init__(self, notebook, name):
        super().__init__(notebook, name)
        # A = load_signal()
        # B = load_signal()
        AplusB = ttk.Button(self.frame, text="A + B",command=self.on_click_addition)
        AminusB = ttk.Button(self.frame, text="A - B",command=self.on_click_subtraction)
        AFold = ttk.Button(self.frame, text="A Fold",command=self.on_click_folding)
        AmulC = ttk.Button(self.frame, text="c × A",command=self.on_click_scaling)
        AdivideB = ttk.Button(self.frame, text="c / A",command=lambda: BasicSignalOperations.divide_signals(signal_a=0,signal_b=0))

        c_label = ttk.Label(self.frame, text="Value of c:")
        self.c = DoubleVar()
        c_input = ttk.Entry(self.frame, textvariable=self.c)

        AplusB.grid(column=0, row=5)
        AminusB.grid(column=1, row=5)
        AFold.grid(column=2, row=5)
        AmulC.grid(column=3, row=5)
        AdivideB.grid(column=4, row=5)

        c_label.grid(column=0, row=6)
        c_input.grid(column=1, row=6, columnspan=3, sticky=(W, E))

    def add(self):
        super().add()  
    
    def on_click_addition(self):
        
        
        if self.A==None or self.B==None:
            show_message_box("title" , "Must Upload two signals First")
        else:
            result_x,result_y = Signal.add_signals(self.A,self.B)
            # current_tab_index = notebook.index(notebook.select())
            # current_tab_frame = notebook.nametowidget(notebook.tabs()[current_tab_index])
            self.Out=Signal(result_x,result_y)
            self.plot_graph(self.ax_out,self.canvas_out,self.Out)  
            #AddSignalSamplesAreEqual("Signal1.txt","Signal2.txt",result_x,result_y)

            # signals['A']['indices'].clear()
            # signals['B']['indices'].clear()
            # signals['A']['samples'].clear()
            # signals['B']['samples'].clear()
    def on_click_subtraction(self):
        if self.A==None or self.B==None:
            show_message_box("title" , "Must Upload two signals First")
        else:
            result_x,result_y = Signal.subtract_signals(self.A,self.B)
            # current_tab_index = notebook.index(notebook.select())
            # current_tab_frame = notebook.nametowidget(notebook.tabs()[current_tab_index])
            self.Out=Signal(result_x,result_y)
            self.plot_graph(self.ax_out,self.canvas_out,self.Out)              #SubSignalSamplesAreEqual("Signal1.txt","Signal2.txt",result_x,result_y)

    def on_click_folding(self):
        if self.A==None:
            show_message_box("title" , "Must Upload signal A First")
        result_x,result_y = Signal.fold_signal(self.A)
        self.Out=Signal(result_x,result_y)
        self.plot_graph(self.ax_out,self.canvas_out,self.Out)          
        #Folding(Your_indices=result_x,Your_samples=result_y)

    def on_click_scaling(self):
        if self.A==None:
            show_message_box("title" , "Must Upload signal A First")
        if self.c==None:
            show_message_box("title" , "Must Enter a value for c")
        result_x,result_y = Signal.scale_signal(self.A,self.c.get())
        self.Out=Signal(result_x,result_y)
        self.plot_graph(self.ax_out,self.canvas_out,self.Out)          
        #Folding(Your_indices=result_x,Your_samples=result_y)

        def on_click_multiply():
            print("C")
            # BasicSignalOperations.multiply_signals(signal_a=sig_A,signal_b=sig_B)

        def on_click_divide():
            print("E")
            # BasicSignalOperations.divide_signals(signal_a=sig_A,signal_b=sig_B)
            
