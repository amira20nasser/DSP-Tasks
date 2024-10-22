from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from ui.ui_widgets import Tab  
from utils import *
from logic.basic_signal_operations import Signal
from task1_test.tests import *
class Task1UI(Tab):
    def __init__(self, notebook, name):
        super().__init__(notebook, name)
        # A = load_signal()
        # B = load_signal()
        input_label = ttk.Label(self.frame, text="Input signals:")

        sig_A= ttk.Button(self.frame,text="Signal A", command=lambda: self.loadSignal('A',self.ax_in,self.canvas_in),bootstyle=SUCCESS)
        sig_B= ttk.Button(self.frame,text="Signal B",command=lambda: self.loadSignal('B',self.ax_in,self.canvas_in),bootstyle=SUCCESS)
        save_output=ttk.Button(self.frame,text="Save Output Signal",command=lambda: self.saveOutput(self.Out,filename_entry.get()),bootstyle=(SUCCESS,OUTLINE))
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

        AplusB = ttk.Button(self.frame, text="A(n) + B(n)",command=self.on_click_addition)
        AminusB = ttk.Button(self.frame, text="A(n) - B(n)",command=self.on_click_subtraction)
        AFold = ttk.Button(self.frame, text="A(-n)",command=self.on_click_folding)
        AmulC = ttk.Button(self.frame, text="cA(n)",command=self.on_click_scaling)
        AshiftC = ttk.Button(self.frame, text="A(n+c)",command=self.on_click_shift)
        op2_label = ttk.Label(self.frame, text="Signal operations:")
        op1_label = ttk.Label(self.frame, text="Operations in variable c:")

        c_label = ttk.Label(self.frame, text="Value of c:")
        self.c = DoubleVar()
        c_input = ttk.Entry(self.frame, textvariable=self.c)
        op2_label.grid(column=0, row=5,sticky=(W, E))
        AplusB.grid(column=1, row=5,sticky=(W, E))
        AminusB.grid(column=2, row=5,sticky=(W, E))
        AFold.grid(column=3, row=5,sticky=(W, E))
        AmulC.grid(column=0, row=8, columnspan=2,sticky=(W, E))
        AshiftC.grid(column=2, row=8,columnspan=2,sticky=(W, E))
        op1_label.grid(column=0,row=6,sticky=(W, E))
        c_label.grid(column=0, row=7,sticky=(W, E))
        c_input.grid(column=1, row=7, columnspan=3, sticky=(W, E))

    def add(self):
        
        super().add()  
    
    def on_click_addition(self):
        
        
        if self.A==None or self.B==None:
            show_message_box("DSP" , "Please upload signals A and B")
        else:
            result_x,result_y = Signal.add_signals(self.A,self.B)
            # current_tab_index = notebook.index(notebook.select())
            # current_tab_frame = notebook.nametowidget(notebook.tabs()[current_tab_index])
            self.Out=Signal(result_x,result_y)
            self.plot_discrete_graph(self.ax_out,self.canvas_out,self.Out,'Output Signal (Sum)')
            AddSignalSamplesAreEqual("Signal1.txt","Signal2.txt",result_x,result_y)
            # signals['A']['indices'].clear()
            # signals['B']['indices'].clear()
            # signals['A']['samples'].clear()
            # signals['B']['samples'].clear()
    def on_click_subtraction(self):
        if self.A==None or self.B==None:
            show_message_box("DSP" , "Please upload signals A and B")
        else:
            result_x,result_y = Signal.subtract_signals(self.A,self.B)
            # current_tab_index = notebook.index(notebook.select())
            # current_tab_frame = notebook.nametowidget(notebook.tabs()[current_tab_index])
            self.Out=Signal(result_x,result_y)
            self.plot_discrete_graph(self.ax_out,self.canvas_out,self.Out,'Output Signal (Difference)')              

            SubSignalSamplesAreEqual("Signal1.txt","Signal2.txt",result_x,result_y)

    def on_click_folding(self):
        if self.A==None:
            show_message_box("DSP" , "Please upload signal A")
        result_x,result_y = Signal.fold_signal(self.A)
        self.Out=Signal(result_x,result_y)
        self.plot_discrete_graph(self.ax_out,self.canvas_out,self.Out,'Output Signal (Folded)')          
        Folding(Your_indices=result_x,Your_samples=result_y)

    def on_click_scaling(self):
        if self.A==None:
            show_message_box("DSP" , "Please upload signal A")
        if self.c==None:
            show_message_box("DSP" , "Please enter a value for c")
        result_x,result_y = Signal.scale_signal(self.A,self.c.get())
        self.Out=Signal(result_x,result_y)
        self.plot_discrete_graph(self.ax_out,self.canvas_out,self.Out,'Output Signal (Scaled by c)')          

        MultiplySignalByConst(5,Your_indices=result_x,Your_samples=result_y)

    def on_click_shift(self):
        if self.A==None:
            show_message_box("DSP" , "Please upload signal A")
        if self.c==None:
            show_message_box("DSP" , "Please enter a value for c")
        result_x,result_y = Signal.shift_signal(self.A,self.c.get())
        self.Out=Signal(result_x,result_y)
        self.plot_discrete_graph(self.ax_out,self.canvas_out,self.Out,'Output Signal (Shifted by c)')      
        #ShiftSignalByConst(-3,Your_indices=result_x,Your_samples=result_y)


