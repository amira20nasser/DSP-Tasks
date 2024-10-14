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
        AplusB = ttk.Button(self.frame, text="A + B",command=lambda: self.on_click_addition(),)
        AminusB = ttk.Button(self.frame, text="A - B",command=lambda: BasicSignalOperations.subtract_signals(signal_a=0,signal_b=0))
        AtimesB = ttk.Button(self.frame, text="A × B",command=lambda: BasicSignalOperations.folding_signal(signal_a=0,signal_b=0))
        AmulC = ttk.Button(self.frame, text="c × A",command=lambda: BasicSignalOperations.scale_signal(signal=0, c=0))
        AdivideB = ttk.Button(self.frame, text="c / A",command=lambda: BasicSignalOperations.divide_signals(signal_a=0,signal_b=0))

        c_label = ttk.Label(self.frame, text="Value of c:")
        c = StringVar()
        c_input = ttk.Entry(self.frame, textvariable=c)

        AplusB.grid(column=0, row=5)
        AminusB.grid(column=1, row=5)
        AtimesB.grid(column=2, row=5)
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
            self.plot_graph(self.ax_out,self.canvas_out,Signal(result_x,result_y,))  
            #AddSignalSamplesAreEqual("Signal1.txt","Signal2.txt",result_x,result_y)

            # signals['A']['indices'].clear()
            # signals['B']['indices'].clear()
            # signals['A']['samples'].clear()
            # signals['B']['samples'].clear()
    def on_click_subtraction(notebook,ax,canvas):
        if not signals['A']['indices'] or not signals['B']['indices']:
            show_message_box("title" , "Must Upload two signals First")
        else:
            result_x,result_y = BasicSignalOperations.subtract_signals(signals['A']['indices'],signals['A']['samples'],signals['B']['indices'],signals['B']['samples'])
            # current_tab_index = notebook.index(notebook.select())
            # current_tab_frame = notebook.nametowidget(notebook.tabs()[current_tab_index])
            plot_graph( result_x,result_y,ax,canvas)  
            SubSignalSamplesAreEqual("Signal1.txt","Signal2.txt",result_x,result_y)

    def on_click_folding(ax,canvas,isSignalA):
        result_x,result_y = BasicSignalOperations.folding_signal(isSignalA=isSignalA,signal=signals)
        plot_graph(result_x,result_y,ax,canvas)  
        Folding(Your_indices=result_x,Your_samples=result_y)


        def on_click_multiply():
            print("C")
            # BasicSignalOperations.multiply_signals(signal_a=sig_A,signal_b=sig_B)
        def on_click_scale():
            print("D")
            # BasicSignalOperations.scale_signal(signal_a=sig_A,signal_b=sig_B)
        def on_click_divide():
            print("E")
            # BasicSignalOperations.divide_signals(signal_a=sig_A,signal_b=sig_B)
            
