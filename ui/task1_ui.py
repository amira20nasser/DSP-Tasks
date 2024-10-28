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
from visualizer import *
from file_manpulator import *

class Task1UI(Tab):
    def initialize_ui_variables(self):
        self.out = None
        self.a_signal = None
        self.b_signal = None
        self.c = DoubleVar()
        self.save_file = StringVar()
        self.file_manpulator = FileManpulator()
        self.input_visualizer = Visualizer(frame=self.frame,title='Input Signal(s)',xlabel='t',ylabel='x(t)')
        self.output_visualizer = Visualizer(frame=self.frame,title='Output Signal',xlabel='t',ylabel='x(t)')

    def __init__(self, notebook, name):
        super().__init__(notebook, name)
        self.initialize_ui_variables()

        input_label = ttk.Label(self.frame, text="Input signals:")
        sig_A_btn= ttk.Button(self.frame,text="Signal A", command=self.on_click_upload_sig_a,bootstyle=SUCCESS)
        sig_B_btn= ttk.Button(self.frame,text="Signal B",command=self.on_click_upload_sig_b,bootstyle=SUCCESS)

        save_output=ttk.Button(self.frame,text="Save Output Signal",command=self.on_click_save_signal,bootstyle=(SUCCESS,OUTLINE))
        clear_output=ttk.Button(self.frame,text="Clear Output",command=self.on_click_clear,bootstyle=(SUCCESS,OUTLINE))
        filename_label = ttk.Label(self.frame, text="Save file name:")
        
        filename_entry = ttk.Entry(self.frame, textvariable=self.save_file)
        self.frame.grid(column=0, row=0,sticky=(W, E))
        input_label.grid(column=0, row=1,sticky=(W, E))
        sig_A_btn.grid(column=0, row=2,columnspan=2,sticky=(W, E))
        sig_B_btn.grid(column=2, row=2,columnspan=2,sticky=(W, E))


        self.input_visualizer.canvas.get_tk_widget().grid(column=0, row=0,columnspan=4)
        self.output_visualizer.canvas.get_tk_widget().grid(column=4, row=0,columnspan=4)

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
    
    def on_click_clear(self):
        self.output_visualizer.clear_plotting()

    def on_click_upload_sig_a(self):
       x,y =  self.file_manpulator.loadSignal()
       self.a_signal = Signal(x,y)
       self.input_visualizer.plot_discrete_graph(signal=self.a_signal)

    def on_click_upload_sig_b(self):
       x,y =  self.file_manpulator.loadSignal()
       self.b_signal = Signal(x,y)
       self.input_visualizer.plot_discrete_graph(signal=self.b_signal)   

    def on_click_save_signal(self):
        self.file_manpulator.saveOutput(signal=self.out,file=self.save_file.get())

    def on_click_addition(self):
        if self.a_signal==None or self.b_signal==None:
            show_message_box("DSP" , "Please upload signals A and B")
        else:
            result_x,result_y = Signal.add_signals(self.a_signal,self.b_signal)
            self.out = Signal(result_x,result_y)

            self.output_visualizer.title = 'Output Signal (Sum)'
            self.output_visualizer.plot_discrete_graph(signal=self.out)
            #Testing
            print("Output Addition Test")
            AddSignalSamplesAreEqual("Signal1.txt","Signal2.txt",result_x,result_y)

    def on_click_subtraction(self):
        if self.a_signal==None or self.b_signal==None:
            show_message_box("DSP" , "Please upload signals A and B")
        else:
            result_x,result_y = Signal.subtract_signals(self.a_signal,self.b_signal)
            self.out = Signal(result_x,result_y)
            
            self.output_visualizer.title = 'Output Signal (Difference)'
            self.output_visualizer.plot_discrete_graph(signal=self.out)
            #Testing
            print("Output Subtraction Test")           
            SubSignalSamplesAreEqual("Signal1.txt","Signal2.txt",result_x,result_y)

    def on_click_folding(self):
        if self.a_signal==None:
            show_message_box("DSP" , "Please upload signal A")

        result_x,result_y = Signal.fold_signal(self.a_signal)
        self.out=Signal(result_x,result_y)

        self.output_visualizer.title = 'Output Signal (Folded)'
        self.output_visualizer.plot_discrete_graph(signal=self.out)
        #Testing
        print("Output Folding Test")                 
        Folding(Your_indices=result_x,Your_samples=result_y)

    def on_click_scaling(self):
        if self.a_signal==None:
            show_message_box("DSP" , "Please upload signal A")
        if self.c==None:
            show_message_box("DSP" , "Please enter a value for c")

        result_x,result_y = Signal.scale_signal(self.a_signal,self.c.get())
        self.out=Signal(result_x,result_y)

        self.output_visualizer.title =  'Output Signal (Scaled by c)'   
        self.output_visualizer.plot_discrete_graph(signal=self.out)
        MultiplySignalByConst(5,Your_indices=result_x,Your_samples=result_y)

    def on_click_shift(self):
        if self.a_signal==None:
            show_message_box("DSP" , "Please upload signal A")
        if self.c==None:
            show_message_box("DSP" , "Please enter a value for c")

        result_x,result_y = Signal.shift_signal(self.a_signal,self.c.get())
        self.out=Signal(result_x,result_y)

        self.output_visualizer.title =  'Output Signal (Shifted by c)'   
        self.output_visualizer.plot_discrete_graph(signal=self.out)
        ShiftSignalByConst(-3,Your_indices=result_x,Your_samples=result_y)


