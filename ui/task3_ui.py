import ttkbootstrap as ttk
from ui.ui_widgets import *
import os
from logic.Quantization import *
from task3_test.QuanTest1 import  *
from task3_test.QuanTest2 import *
from visualizer import *
from file_manpulator import *

class Task3UI(Tab):
    def initialize_ui_variables(self):       
        # self.save_file = StringVar()
        self.error=None
        self.sampled_signal = None
        self.quantized_signal = None
        self.levels = IntVar()
        self.bits = IntVar()
        self.file_manpulator = FileManpulator()
        self.isSelectedLevels = BooleanVar()
        self.original_visualizer = Visualizer(self.frame,'Input Sampled Signal(s)','n','x(n)')
        self.quantized_visualizer = Visualizer(self.frame,'Quantized Signal','n','x_q(n)')
        self.error_visualizer = Visualizer(self.frame,'Quantization Error','n','error_q')

    def __init__(self,notebook,name):
        super().__init__(notebook,name)
        self.initialize_ui_variables()

        self.original_visualizer.canvas.get_tk_widget().grid(column=0, row=0,)
        self.quantized_visualizer.canvas.get_tk_widget().grid(column=1, row=0,)
        self.error_visualizer.canvas.get_tk_widget().grid(column=2, row=0,)

        upload_sampled_sig = ttk.Button(master=self.frame, text="Upload Sampled Signal",command=self.on_click_upload) 
        upload_sampled_sig.grid(column=0,row=1,sticky=(W))

        self.isSelectedLevels.set(True)
        radio_levels = ttk.Radiobutton(self.frame,text="#Levels", variable=self.isSelectedLevels,value=1,command=self.toggle_input)
        self.levels_entry = ttk.Entry(self.frame,state=["normal"],textvariable=self.levels)

        radio_levels.grid(column=0,row=2,sticky=(W),)
        self.levels_entry.grid(column=0,row=3, sticky=(W))

        radio_bits = ttk.Radiobutton(self.frame,text="#bits", variable=self.isSelectedLevels,value=0,command=self.toggle_input)
        self.bits_entry = ttk.Entry(self.frame,state=["disabled"],textvariable=self.bits)
        radio_bits.grid(column=0,row=4,sticky=(W))
        self.bits_entry.grid(column=0,row=5, sticky=(W),)

        quantized_sig = ttk.Button(master=self.frame, text="Show Quantized Signal",command=self.on_click_quantized) 
        quantized_sig.grid(column=1,row=1,sticky=(W))

        # save_output=ttk.Button(self.frame,text="Save Output",command=lambda: self.saveOutput(self.encoded_indices,self.Out,filename_entry.get()),bootstyle=(SUCCESS,OUTLINE))
        clear_output=ttk.Button(self.frame,text="Clear Quantized Output",command=self.quantized_visualizer.clear_plotting,bootstyle=(SUCCESS,OUTLINE))
        # save_output.grid(column=1,row=2,sticky=(W))
        clear_output.grid(column=1,row=3,sticky=(W))
        # filename_label = ttk.Label(self.frame, text="Save file name:")
        # filename_entry = ttk.Entry(self.frame, textvariable=self.save_file)
        # filename_label.grid(column=1,row=4,sticky=(W))
        # filename_entry.grid(column=1,row=5,sticky=(W))
        
        err_sig = ttk.Button(master=self.frame, text="Show Error",command=self.on_click_show_err) 
        err_sig.grid(column=2,row=1,sticky=(W))

    def toggle_input(self):
        if self.isSelectedLevels.get():
            self.levels_entry.config(state=['normal'])
            self.bits_entry.config(state=['disabled'])
        else:
            self.levels_entry.config(state=['disabled'])
            self.bits_entry.config(state=['normal'])     
    
    
    def on_click_upload(self):
        x,y = self.file_manpulator.loadSignal()
        self.sampled_signal = Signal(x,y)
        self.original_visualizer.plot_discrete_graph(self.sampled_signal)
    def on_click_quantized(self):
        if self.sampled_signal == None or (self.levels_entry.get()==None and self.bits_entry==None):
            messagebox.showerror("DSP", "MUST ENTER ALL VALUES sampled_sig,#levels,#bits")
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



    
