import ttkbootstrap as ttk
from ui.ui_widgets import *
import os
from logic.convolution import *
from visualizer import *
from file_manpulator import *

class Task4UI(Tab):
    def initialize_ui_variables(self):       
        self.sampled_signal = None
        self.average_signal = None
        self.window_size = IntVar(value=3)
        self.file_manpulator = FileManpulator()
        self.avg_signal_visualizer = Visualizer(self.frame,'Average','n','y(n)')
        self.derivative_visualizer = Visualizer(self.frame,'Drivative','n','y(n)')
        self.original_visualizer = Visualizer(self.frame,'Input Sampled Signal(s)','n','x(n)')
        # self.bits = IntVar()
        # self.isSelectedLevels = BooleanVar()

    def __init__(self,notebook,name):
        super().__init__(notebook,name)
        self.initialize_ui_variables()

        self.original_visualizer.canvas.get_tk_widget().grid(column=0, row=0,)
        self.avg_signal_visualizer.canvas.get_tk_widget().grid(column=1, row=0,)
        self.derivative_visualizer.canvas.get_tk_widget().grid(column=2, row=0,)

        upload_sampled_sig = ttk.Button(master=self.frame, text="Upload Sampled Signal",command=self.on_click_upload) 
        upload_sampled_sig.grid(column=0,row=1,sticky=(W))

        w_label = ttk.Label(self.frame, text="Window Size")
        w_label.grid(column=0,row=2, sticky=(W))
        window_size_entry = ttk.Entry(self.frame,textvariable=self.window_size)
        window_size_entry.grid(column=0,row=3, sticky=(W))

        # radio_bits = ttk.Radiobutton(self.frame,text="#bits", variable=self.isSelectedLevels,value=0,command=self.toggle_input)
        # self.bits_entry = ttk.Entry(self.frame,state=["disabled"],textvariable=self.bits)
        # radio_bits.grid(column=0,row=4,sticky=(W))
        # self.bits_entry.grid(column=0,row=5, sticky=(W),)

        avg_sig = ttk.Button(master=self.frame, text="Compute Avg",command=self.on_click_avg_signal) 
        avg_sig.grid(column=1,row=1,sticky=(W))

        drev1_sig = ttk.Button(master=self.frame, text="First Drivative",command=self.on_click_first_derivative_signal) 
        drev1_sig.grid(column=2,row=1,sticky=(W))

        drev2_sig = ttk.Button(master=self.frame, text="Second Drivative",command=self.on_click_second_derivative_signal) 
        drev2_sig.grid(column=2,row=2,sticky=(W))
        # clear_output=ttk.Button(self.frame,text="Clear Quantized Output",command=self.quantized_visualizer.clear_plotting,bootstyle=(SUCCESS,OUTLINE))
        # clear_output.grid(column=1,row=3,sticky=(W))
       
        
        # err_sig = ttk.Button(master=self.frame, text="Show Error",command=self.on_click_show_err) 
        # err_sig.grid(column=2,row=1,sticky=(W))

    # def toggle_input(self):
    #     if self.isSelectedLevels.get():
    #         self.levels_entry.config(state=['normal'])
    #         self.bits_entry.config(state=['disabled'])
    #     else:
    #         self.levels_entry.config(state=['disabled'])
    #         self.bits_entry.config(state=['normal'])     
    
    
    def on_click_upload(self):
        x,y = self.file_manpulator.loadSignal()
        self.sampled_signal = Signal(x,y)
        self.original_visualizer.plot_discrete_graph(self.sampled_signal)

    def on_click_avg_signal(self):
        self.average_signal = Convolution.compute_average(self.sampled_signal,self.window_size.get())
        self.avg_signal_visualizer.plot_discrete_graph(self.average_signal)

    def on_click_first_derivative_signal(self):
        self.first_drev, _ =  Convolution.sharpening_sig(self.sampled_signal)
        self.derivative_visualizer.clear_plotting()
        self.derivative_visualizer.plot_discrete_graph(self.first_drev)
    
    def on_click_second_derivative_signal(self):
        _, self.second_drev =  Convolution.sharpening_sig(self.sampled_signal)
        self.derivative_visualizer.clear_plotting()
        self.derivative_visualizer.plot_discrete_graph(self.second_drev)
    
    # def on_click_show_err(self):
    #     error = Quatization.calculate_error(self.quantized_signal.y , self.sampled_signal.y)
    #     self.error_visualizer.plot_continous_graph(Signal(self.sampled_signal.x,error))
 
