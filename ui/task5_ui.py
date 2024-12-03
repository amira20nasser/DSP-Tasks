import ttkbootstrap as ttk
from ui.ui_widgets import *
import os
from logic.Quantization import *
from task3_test.QuanTest1 import  *
from task3_test.QuanTest2 import *
from visualizer import *
from file_manpulator import *
from logic.fourier_transform import *
import math 
class Task5UI(Tab):
    def initialize_ui_variables(self):       
        # self.save_file = StringVar()
        self.error=None
        self.time_domain_signal = None
        self.frequency_domain_signal = None
        self.fs = IntVar()
        self.file_manpulator = FileManpulator()
        self.time_amplitude_visualizer = Visualizer(self.frame,'Time Domain Signal','n','x(n)')
        self.frequency_amplitude_visualizer = Visualizer(self.frame,'Frequency Domain (Amplitude)','k','x(k)')
        self.frequency_phase_visualizer = Visualizer(self.frame,'Frequency Domain (Phase)','n','x_q(n)')

    def __init__(self,notebook,name):
        super().__init__(notebook,name)
        self.initialize_ui_variables()

        self.time_amplitude_visualizer.canvas.get_tk_widget().grid(column=0, row=0,)
        self.frequency_amplitude_visualizer.canvas.get_tk_widget().grid(column=1, row=0,)
        self.frequency_phase_visualizer.canvas.get_tk_widget().grid(column=1, row=2,)

        upload_time_sig = ttk.Button(master=self.frame, text="Upload Time Signal",command=lambda:self.on_click_upload(True)) 
        upload_time_sig.grid(column=0,row=2,sticky=(W))

        upload_freq_sig = ttk.Button(master=self.frame, text="Upload Frequency Signal",command=lambda: self.on_click_upload(False)) 
        upload_freq_sig.grid(column=0,row=3,sticky=(W))


        self.fs_entry = ttk.Entry(master=self.frame,textvariable=self.fs)
        self.fs_entry.grid(column=0,row=1, sticky=(W),)

        dft = ttk.Button(master=self.frame, text="DFT",command=self.on_click_dft) 
        dft.grid(column=1,row=2,sticky=(W))

        idft = ttk.Button(master=self.frame, text="IDFT",command=self.on_click_idft) 
        idft.grid(column=1,row=1,sticky=(W))

    
    def on_click_upload(self,time_domain):
        x,y = self.file_manpulator.loadSignal()
        if time_domain:
            self.fs.set(len(x))
            self.time_domain_signal = Signal(x,y)
            self.time_amplitude_visualizer.plot_discrete_graph(self.time_domain_signal)

        else:
            self.frequency_domain_signal=Signal(x,y)
            n=2*math.pi*self.fs.get()/len(x)
            k= [n*i for i in range(len(x))]
            self.frequency_amplitude_visualizer.plot_discrete_graph(Signal(k,x))
            self.frequency_phase_visualizer.plot_discrete_graph(Signal(k,y))

    def on_click_dft(self):
        if self.time_domain_signal == None:
            messagebox.showerror("DSP", "MUST ENTER SIGNAL")
            return

        amp, phase =  FourierTransform.dtf_transform(self.time_domain_signal.y,self.fs.get())
        n = 2*math.pi*self.fs.get()/len(self.time_domain_signal.x)
        k= [n*i for i in range(len(self.time_domain_signal.x))]
        self.frequency_amplitude_visualizer.clear_plotting()
        self.frequency_phase_visualizer.clear_plotting()
        self.frequency_amplitude_visualizer.plot_discrete_graph(Signal(k,amp))
        self.frequency_phase_visualizer.plot_discrete_graph(Signal(k,phase))


    def on_click_idft(self):
        if self.frequency_domain_signal == None:
            messagebox.showerror("DSP", "MUST ENTER SIGNAL")
            return   
        self.time_domain_signal= FourierTransform.idtf_transform(self.frequency_domain_signal.x,self.frequency_domain_signal.y)
        x=[i for i in range(len(self.time_domain_signal))]
        self.time_amplitude_visualizer.plot_discrete_graph(Signal(x,self.time_domain_signal))

    
