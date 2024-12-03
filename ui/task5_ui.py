import ttkbootstrap as ttk
from ui.ui_widgets import *
import os
from logic.Quantization import *
from task3_test.QuanTest1 import  *
from task3_test.QuanTest2 import *
from visualizer import *
from file_manpulator import *

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
        dft.grid(column=1,row=1,sticky=(W))

        idft = ttk.Button(master=self.frame, text="IDFT",command=self.on_click_idft) 
        idft.grid(column=1,row=1,sticky=(W))

    def toggle_input(self):
        if self.isSelectedLevels.get():
            self.levels_entry.config(state=['normal'])
            self.bits_entry.config(state=['disabled'])
        else:
            self.levels_entry.config(state=['disabled'])
            self.bits_entry.config(state=['normal'])     
    
    
    def on_click_upload(self,time_domain):
        x,y = self.file_manpulator.loadSignal()
        if time_domain:
            self.time_domain_signal = Signal(x,y)
            self.time_amplitude_visualizer.plot_discrete_graph(self.time_domain_signal)

        else:
            self.frequency_domain_signal=Signal(x,y)
            n=2*math.pi*fs/len(x)
            self.k= [n*i for i in range(len(x))]
            self.frequency_amplitude_visualizer.plot_discrete_graph(Signal(self.k,x))
            self.frequency_phase_visualizer.plot_discrete_graph(Signal(self.k,y))

    def on_click_dft(self):
        if self.time_domain_signal == None:
            messagebox.showerror("DSP", "MUST ENTER SIGNAL")
            return   
    def on_click_idft(self):
        if self.frequency_domain_signal == None:
            messagebox.showerror("DSP", "MUST ENTER SIGNAL")
            return   

        index_intervals,x_q,encoded_index = [],[] ,[]
        if self.isSelectedLevels.get(): 
            interval_index,x_q,encoded_index = Quatization.quantize_signal(self.sampled_signal,self.levels.get())
        else:
            interval_index,x_q,encoded_index = Quatization.quantize_signal(self.sampled_signal,2**self.bits.get())
        
        self.quantized_signal=Signal(self.sampled_signal.x , x_q)
        self.quantized_visualizer.plot_discrete_graph(signal=self.quantized_signal)
        QuantizationTest1("task3\Test 1\Quan1_Out.txt",encoded_index,x_q)
        QuantizationTest2("task3\Test 2\Quan2_Out.txt",interval_index,encoded_index,x_q,Quatization.calculate_error(self.quantized_signal.y , self.sampled_signal.y))

    def on_click_show_err(self):
        error = Quatization.calculate_error(self.quantized_signal.y , self.sampled_signal.y)
        self.error_visualizer.plot_continous_graph(Signal(self.sampled_signal.x,error))

    # def saveOutput(self, interval_indices, quantized_values, file):
    #     if interval_indices == None or quantized_values == None:
    #         show_message_box("DSP" , "No output signal to save")
    #     elif not file :
    #         show_message_box("DSP" , "Please enter save file name")
    #     else:
    #         with open(file, 'w') as f:
    #             # Write header information
    #             f.write('0\n0\n' + str(len(interval_indices)) + '\n')
                
    #             # Iterate through both arrays and write to file
    #             for interval_index, quantized_value in zip(interval_indices, quantized_values):
    #                 f.write(f"{interval_index} {quantized_value}\n")

    #         show_message_box("DSP" , "Signal saved successfully")



    
