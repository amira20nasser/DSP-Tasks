from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.ui_widgets import Tab  
from logic.generate_sin_cos import *
from logic.basic_signal_operations import Signal
from utils import *
from visualizer import *
from file_manpulator import *

class Task2UI(Tab):
    def initialize_ui_variables(self):
        self.shifted = DoubleVar()
        self.fs= IntVar()
        self.discrete_out = None
        self.continous_out = None
        self.sig_interpolate = None
        self.freq = IntVar()
        self.amplitude = IntVar()
        self.save_file = StringVar()
        self.file_manpulator = FileManpulator()
        self.selected_type = StringVar(value=Type.SIN.name)
        self.wave_visualizer = Visualizer(frame=self.frame,title='Input Signal(s)',xlabel='t',ylabel='x(t)')
        self.wave_sampled_visualizer = Visualizer(frame=self.frame,title='Wave Signal',xlabel='t',ylabel='x(t)')
        self.interpolate_visualizer = Visualizer(frame=self.frame,title='Sampled Wave',xlabel='t',ylabel='x(t)')

    def __init__(self, notebook, name):
        super().__init__(notebook, name)
        self.initialize_ui_variables()

        read_input= ttk.Button(self.frame,text="Read Input", command=self.on_click_upload_sig)
        interpolate_input= ttk.Button(self.frame,text="Interpolate Input",command=self.on_click_interpolate)
    
        save_interpolation_output=ttk.Button(self.frame,text="Save Interpolation",command=lambda:self.on_click_save_signal(self.sig_interpolate),bootstyle=(SUCCESS,OUTLINE))
        clear_interpolation_output=ttk.Button(self.frame,text="Clear Interpolation",command=self.interpolate_visualizer.clear_plotting,bootstyle=(SUCCESS,OUTLINE))
        filename_label = ttk.Label(self.frame, text="Save file name:")
        filename_entry = ttk.Entry(self.frame, textvariable=self.save_file)
        self.frame.grid(column=0, row=0,sticky=(W, E))

        self.wave_visualizer.canvas.get_tk_widget().grid(column=0, row=0,columnspan=4)
        self.wave_sampled_visualizer.canvas.get_tk_widget().grid(column=4, row=0,columnspan=4)
        self.interpolate_visualizer.canvas.get_tk_widget().grid(column=8, row=0,columnspan=4)

        filename_label.grid(column=0, row=1,sticky=(W, E))
        filename_entry.grid(column=1, row=1, columnspan=3, sticky=(W, E))

        label = ttk.Label(self.frame,text="Please select type:")
        label.grid(column=0, row=3,columnspan=2,sticky=(W, E))
        type_cb = ttk.Combobox(self.frame, textvariable=self.selected_type)
        type_cb['values'] = [Type.SIN.name,Type.COS.name]
        # prevent user typing a value
        type_cb['state'] = 'readonly'
        type_cb.grid(column=1, row=3,sticky=(W, E))

        amplitude_label = ttk.Label(self.frame, text="Amplitude")
        amplitude_label.grid(column=0, row=5,columnspan=2,sticky=(W, E))
        amplitude_input = ttk.Entry(self.frame, textvariable=self.amplitude)
        amplitude_input.insert(1, 1)

        amplitude_input.grid(column=0, row=6, columnspan=1,sticky=(N, W, E, S))

        freq_label = ttk.Label(self.frame, text="Frequency")
        freq_label.grid(column=1, row=5,columnspan=2,sticky=(W, E))
        freq_input = ttk.Entry(self.frame, textvariable=self.freq)
        freq_input.insert(1, 1)

        freq_input.grid(column=1, row=6, columnspan=1, sticky=(W, E))

        shifted_label = ttk.Label(self.frame, text="Shifted By")
        shifted_label.grid(column=2, row=5,columnspan=2,sticky=(W, E))
        shifted_input = ttk.Entry(self.frame, textvariable=self.shifted)
        shifted_input.grid(column=2, row=6, columnspan=1,sticky=(N, W, E, S))

        generate_btn = ttk.Button(self.frame, text="Generate SIN / COS",command=self.on_click_generate)
        generate_btn.grid(column=0, row=7,columnspan=3,sticky=(W, E))
        save_sin_output=ttk.Button(self.frame,text="Save Sampled Sinosoidal",command=lambda: self.on_click_save_signal(self.discrete_out),bootstyle=(SUCCESS,OUTLINE))

        label = ttk.Label(self.frame,text="F_s")
        label.grid(column=0, row=8,columnspan=1,sticky=(W, E))
        
        fs_input = ttk.Entry(self.frame, textvariable=self.fs)
        fs_input.grid(column=1, row=8, columnspan=1,sticky=(N, W, E, S))
        sampling_btn = ttk.Button(self.frame, text=f"Sampling {self.selected_type.get()} Wave",command=self.on_click_Sampling)
        sampling_btn.grid(column=0, row=9,columnspan=3,sticky=(W, E))
        save_sin_output.grid(column=0, row=10,columnspan=4,sticky=(W, E))
        read_input.grid(column=8,row=1,columnspan=2,sticky=(W, E))
        interpolate_input.grid(column=10,row=1,columnspan=2,sticky=(W, E))
        save_interpolation_output.grid(column=8,row=2,columnspan=2,sticky=(W, E))
        clear_interpolation_output.grid(column=10,row=2,columnspan=2,sticky=(W, E))

    def on_click_upload_sig(self):
       x,y =  self.file_manpulator.loadSignal()
       signal = Signal(x,y)
       self.sig_interpolate = signal
       self.interpolate_visualizer.plot_discrete_graph(signal=signal)

    def on_click_interpolate(self):
        self.interpolate_visualizer.interpolate( self.sig_interpolate)
    
    def on_click_save_signal(self,signal):
        self.file_manpulator.saveOutput( signal,self.save_file.get())

    def on_click_generate(self):
        t,x_t = GenerateSinCos.generate_sin_cos(Type[self.selected_type.get()],self.amplitude.get(),self.freq.get(),self.shifted.get())
        signal = Signal(t,x_t)
        self.continous_out = signal
        self.wave_visualizer.title = f"{self.selected_type.get()} Signal"
        self.wave_visualizer.plot_continous_graph(signal = signal)

    def on_click_Sampling(self):
        if self.fs.get() < 2*self.freq.get():
            show_message_box("ERROR" , f"fs must be at least {2*self.freq.get()} ")
            return
        n,x_n = GenerateSinCos.sampling_sin_cos(Type[self.selected_type.get()],self.amplitude.get(),self.freq.get(),self.shifted.get(),self.fs.get())
        signal = Signal(n,x_n)
        self.discrete_out = signal
        self.wave_sampled_visualizer.title = f"Sampling {self.selected_type.get()} Signal"
        self.wave_sampled_visualizer.plot_discrete_graph(signal=signal)



