import ttkbootstrap as ttk
from ui.ui_widgets import *
import os
from logic.convolution import *
from visualizer import *
from file_manpulator import *
from task4_test.testT4 import *

class Task4UI(Tab):
    def initialize_ui_variables(self):       
        self.sampled_signal = None
        self.average_signal = None
        self.window_size = IntVar(value=3)
        self.file_manpulator = FileManpulator()
        self.avg_signal_visualizer = Visualizer(self.frame,'Average','n','y(n)')
        self.derivative_visualizer = Visualizer(self.frame,'Drivative','n','y(n)')
        self.original_visualizer = Visualizer(self.frame,'Input Sampled Signal(s)','n','x(n)')
        self.con_visualizer = Visualizer(self.frame,'Convolution','n','y(n)')
    def __init__(self,notebook,name):
        super().__init__(notebook,name)
        self.initialize_ui_variables()

        self.original_visualizer.canvas.get_tk_widget().grid(column=0, row=0,)
        self.avg_signal_visualizer.canvas.get_tk_widget().grid(column=1, row=0,)
        self.derivative_visualizer.canvas.get_tk_widget().grid(column=2, row=0,)
        self.con_visualizer.canvas.get_tk_widget().grid(column=2,row=5,)

        upload_sampled_sig = ttk.Button(master=self.frame, text="Upload Sampled Signal",command=self.on_click_upload) 
        upload_sampled_sig.grid(column=0,row=1,sticky=(W))
        
        w_label = ttk.Label(self.frame, text="Window Size")
        w_label.grid(column=0,row=2, sticky=(W))
        window_size_entry = ttk.Entry(self.frame,textvariable=self.window_size)
        window_size_entry.grid(column=0,row=3, sticky=(W))

        avg_sig = ttk.Button(master=self.frame, text="Compute Avg",command=self.on_click_avg_signal) 
        avg_sig.grid(column=1,row=1,sticky=(W))

        drev1_sig = ttk.Button(master=self.frame, text="First Drivative",command=self.on_click_first_derivative_signal) 
        drev1_sig.grid(column=2,row=1,sticky=(W))

        drev2_sig = ttk.Button(master=self.frame, text="Second Drivative",command=self.on_click_second_derivative_signal) 
        drev2_sig.grid(column=2,row=2,sticky=(W))

        conv_btn = ttk.Button(master=self.frame, text="CONV",command=self.on_click_convolution) 
        conv_btn.grid(column=1,row=2,sticky=(W))
    
        upload_sampled_sig_1 = ttk.Button(master=self.frame, text="Upload Sampled Signal 1",command=self.on_click_upload_sig1) 
        upload_sampled_sig_1.grid(column=0,row=5,sticky=(W))
        
        upload_sampled_sig_2 = ttk.Button(master=self.frame, text="Upload Sampled Signal 2",command=self.on_click_upload_sig2) 
        upload_sampled_sig_2.grid(column=1,row=5,sticky=(W))
        
    def on_click_upload(self):
        x,y = self.file_manpulator.loadSignal()
        self.sampled_signal = Signal(x,y)
        self.original_visualizer.clear_plotting()
        self.original_visualizer.plot_discrete_graph(self.sampled_signal)
    
    def on_click_upload_sig1(self):
        x,y = self.file_manpulator.loadSignal()
        self.sig1 = Signal(x,y)
        self.original_visualizer.title = "Sig 1"
        self.original_visualizer.clear_plotting()
        self.original_visualizer.plot_discrete_graph(self.sig1)
    
    def on_click_upload_sig2(self):
        x,y = self.file_manpulator.loadSignal()
        self.sig2 = Signal(x,y)
        self.avg_signal_visualizer.title = "Sig2"
        self.avg_signal_visualizer.clear_plotting()
        self.avg_signal_visualizer.plot_discrete_graph(self.sig2)
   

    def on_click_avg_signal(self):
        self.average_signal = Convolution.compute_average(self.sampled_signal,self.window_size.get())
        self.avg_signal_visualizer.plot_discrete_graph(self.average_signal)
        test_task4("task4_test\Moving Average testcases\MovingAvg_out1.txt",self.average_signal.x,self.average_signal.y)
    
    def on_click_first_derivative_signal(self):
        self.first_drev, _ =  Convolution.sharpening_sig(self.sampled_signal)
        self.derivative_visualizer.clear_plotting()
        self.derivative_visualizer.plot_discrete_graph(self.first_drev)
        test_task4("task4_test\Derivative testcases\\1st_derivative_out.txt",self.first_drev.x,self.first_drev.y)
        
    def on_click_second_derivative_signal(self):
        _, self.second_drev =  Convolution.sharpening_sig(self.sampled_signal)
        self.derivative_visualizer.clear_plotting()
        self.derivative_visualizer.plot_discrete_graph(self.second_drev)
        test_task4("task4_test\Derivative testcases\\2nd_derivative_out.txt",self.second_drev.x,self.second_drev.y)
        
    def on_click_convolution(self):
        s= Convolution.convolve(self.sig1,self.sig2)
        self.con_visualizer.clear_plotting()
        self.con_visualizer.plot_discrete_graph(s)
        test_task4("task4_test\Convolution testcases\Conv_output.txt",s.x,s.y)
