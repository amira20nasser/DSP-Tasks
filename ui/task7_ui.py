from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.ui_widgets import Tab  
from logic.filters import *
from logic.basic_signal_operations import Signal
from utils import *
from visualizer import *
from file_manpulator import *

class Task7UI(Tab):
    def initialize_ui_variables(self):
        self.input = None
        self.output = None
        self.save_file = StringVar()
        self.file_manpulator = FileManpulator()
        self.selected_type = StringVar(value=Type.LOW_PASS.value)
        self.input_visualizer = Visualizer(frame=self.frame,title='Input Signal',xlabel='t',ylabel='x(t)')
        self.output_visualizer = Visualizer(frame=self.frame,title='Filtered Signal',xlabel='t',ylabel='x(t)')

    def __init__(self, notebook, name):
        super().__init__(notebook, name)
        self.initialize_ui_variables()

        read_input= ttk.Button(self.frame,text="Read Signal", command=self.on_click_upload_sig,bootstyle=(SUCCESS))
        apply_filter= ttk.Button(self.frame,text="Apply Filter",command=self.on_click_apply_filter)
    
        save_output=ttk.Button(self.frame,text="Save Output",command=lambda:self.on_click_save_signal(self.output),bootstyle=(SUCCESS,OUTLINE))
        clear_output=ttk.Button(self.frame,text="Clear Output",command=self.output_visualizer.clear_plotting,bootstyle=(SUCCESS,OUTLINE))
        filename_label = ttk.Label(self.frame, text="Save file name:")
        filename_entry = ttk.Entry(self.frame, textvariable=self.save_file)
        self.frame.grid(column=0, row=0,sticky=(W, E))

        self.input_visualizer.canvas.get_tk_widget().grid(column=0, row=0,columnspan=4)
        self.output_visualizer.canvas.get_tk_widget().grid(column=4, row=0,columnspan=4)

        filename_label.grid(column=4, row=1,sticky=(W, E))
        filename_entry.grid(column=5, row=1, columnspan=3, sticky=(W, E))

        label = ttk.Label(self.frame,text="Please select type:")
        label.grid(column=0, row=2,columnspan=2,sticky=(W, E))
        type_cb = ttk.Combobox(self.frame, textvariable=self.selected_type)
        type_cb['values'] = [Type.LOW_PASS.value,Type.HIGH_PASS.value,Type.BAND_PASS.value,Type.BAND_REJECT.value]
        # prevent user typing a value
        type_cb['state'] = 'readonly'
        type_cb.grid(column=1, row=2,sticky=(W, E),columnspan=3)


        read_input.grid(column=0,row=1,columnspan=2,sticky=(W, E))
        apply_filter.grid(column=2,row=1,columnspan=2,sticky=(W, E))
        save_output.grid(column=4,row=2,columnspan=2,sticky=(W, E))
        clear_output.grid(column=6,row=2,columnspan=2,sticky=(W, E))

    def on_click_upload_sig(self):
       x,y =  self.file_manpulator.loadSignal()
       signal = Signal(x,y)
       self.input_visualizer.plot_discrete_graph(signal=signal)

    def on_click_apply_filter(self):
        print("")
    
    def on_click_save_signal(self,signal):
        self.file_manpulator.saveOutput( signal,self.save_file.get())



