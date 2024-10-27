import ttkbootstrap as ttk
from ui.ui_widgets import *
import os
from logic.Quantization import *

class Task3UI(Tab):
    def __init__(self,notebook,name):
        super().__init__(notebook,name)
        self.interval_indices=None
        self.encoded_indices=None
        self.error=None
        self.fig_original, self.ax_original, self.canvas_original = self.initialize_graph('Input Sampled Signal(s)','n','x(n)')
        self.fig_quantized,self.ax_quantized, self.canvas_quantized = self.initialize_graph('Quantized Signal','-','x_q(n)')
        self.fig_error, self.ax_error, self.canvas_error = self.initialize_graph('Quantization Error','x_q(n)','error_q')

        self.canvas_original.get_tk_widget().grid(column=0, row=0,)
        self.canvas_quantized.get_tk_widget().grid(column=1, row=0,)
        self.canvas_error.get_tk_widget().grid(column=2, row=0,)


        upload_sampled_sig = ttk.Button(master=self.frame, text="Upload Sampled Signal",command=self.on_click_upload) 
        upload_sampled_sig.grid(column=0,row=1,sticky=(W))

        self.isSelectedLevels = BooleanVar()
        self.isSelectedLevels.set(True)
        radio_levels = ttk.Radiobutton(self.frame,text="#Levels", variable=self.isSelectedLevels,value=1,command=self.toggle_input)
        self.levels = IntVar()
        self.levels_entry = ttk.Entry(self.frame,state=["normal"],textvariable=self.levels)

        radio_levels.grid(column=0,row=2,sticky=(W),)
        self.levels_entry.grid(column=0,row=3, sticky=(W))

        radio_bits = ttk.Radiobutton(self.frame,text="#bits", variable=self.isSelectedLevels,value=0,command=self.toggle_input)
        self.bits = IntVar()
        self.bits_entry = ttk.Entry(self.frame,state=["disabled"],textvariable=self.bits)
        radio_bits.grid(column=0,row=4,sticky=(W))
        self.bits_entry.grid(column=0,row=5, sticky=(W),)

        quantized_sig = ttk.Button(master=self.frame, text="Show Quantized Signal",command=self.on_click_quantized) 
        quantized_sig.grid(column=1,row=1,sticky=(W))

        save_output=ttk.Button(self.frame,text="Save Output",command=lambda: self.saveOutput(self.encoded_indices,self.Out,filename_entry.get()),bootstyle=(SUCCESS,OUTLINE))
        clear_output=ttk.Button(self.frame,text="Clear Output",command=lambda:self.clearOutput('Out',self.ax_quantized,self.canvas_quantized),bootstyle=(SUCCESS,OUTLINE))
        save_output.grid(column=1,row=2,sticky=(W))
        clear_output.grid(column=1,row=3,sticky=(W))
        filename_label = ttk.Label(self.frame, text="Save file name:")
        self.save_file = StringVar()
        filename_entry = ttk.Entry(self.frame, textvariable=self.save_file)
        filename_label.grid(column=1,row=4,sticky=(W))
        filename_entry.grid(column=1,row=5,sticky=(W))

    def toggle_input(self):
        if self.isSelectedLevels.get():
            self.levels_entry.config(state=['normal'])
            self.bits_entry.config(state=['disabled'])
        else:
            self.levels_entry.config(state=['disabled'])
            self.bits_entry.config(state=['normal'])     
    
    
    def on_click_upload(self):
        self.loadSignal(ax=self.ax_original,sig="A",canvas=self.canvas_original)

    def on_click_quantized(self):
        if self.A == None or (self.levels_entry.get()==None and self.bits_entry==None):
            messagebox.showinfo("DSP", "MUST ENTER ALL VALUES sampled_sig,#levels,#bits")
            return   
        index_intervals,x_q = [],[]  
        if self.isSelectedLevels.get(): 
            interval_index,x_q,encoded_index,error = Quatization.quantize_signal(self.A,self.levels.get())
        else:
            interval_index,x_q,encoded_index,error = Quatization.quantize_signal(self.A,2**self.bits.get())

        # self.ax_quantized.plot(self.A.x, x_q),
        # self.canvas_quantized.draw()
        self.Out=Signal(self.A.x,x_q)
        self.interval_indices=interval_index
        self.encoded_indices=encoded_index
        self.plot_discrete_graph(self.ax_quantized,self.canvas_quantized,self.Out, "Qauntized Signal")
        self.ax_quantized.set_xlabel('n')
    def saveOutput(self, interval_indices, quantized_values, file):
        if interval_indices == None or quantized_values == None:
            show_message_box("DSP" , "No output signal to save")
        elif not file :
            show_message_box("DSP" , "Please enter save file name")
        else:
            with open(file, 'w') as f:
                # Write header information
                f.write('0\n0\n' + str(len(interval_indices)) + '\n')
                
                # Iterate through both arrays and write to file
                for interval_index, quantized_value in zip(interval_indices, quantized_values):
                    f.write(f"{interval_index} {quantized_value}\n")

            show_message_box("DSP" , "Signal saved successfully")



    
