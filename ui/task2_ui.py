import numpy as np
from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from ui.ui_widgets import Tab  
from logic.generate_sin_cos import *
from logic.basic_signal_operations import Signal
from utils import *
from scipy.interpolate import interp1d

class Task2UI(Tab):
    def __init__(self, notebook, name):
        
        super().__init__(notebook, name)
        read_input= ttk.Button(self.frame,text="Read Input", command=lambda: self.loadSignal('A',self.ax_int,self.canvas_int))
        interpolate_input= ttk.Button(self.frame,text="Interpolate Input",command=lambda: self.interpolate(self.ax_int,self.canvas_int,self.A,''))
        self.continous_out = None
        self.discrete_out = None

        save_interpolation_output=ttk.Button(self.frame,text="Save Interpolation",command=lambda: self.saveOutput(self.Interpolation,filename_entry.get()),bootstyle=(SUCCESS,OUTLINE))
        clear__interpolation_output=ttk.Button(self.frame,text="Clear Interpolation",command=lambda:self.clearOutput('Interpolation',self.ax_int,self.canvas_int),bootstyle=(SUCCESS,OUTLINE))
        filename_label = ttk.Label(self.frame, text="Save file name:")
        self.save_file = StringVar()
        filename_entry = ttk.Entry(self.frame, textvariable=self.save_file)
        self.frame.grid(column=0, row=0,sticky=(W, E))
        self.fig_int, self.ax_int, self.canvas_int = self.initialize_graph('Input Signal','t','x(t)')
        self.fig_sin,self.ax_sin, self.canvas_sin = self.initialize_graph('Sinosoidal Signal','t','x(t)')
        self.fig_sin_sampled,self.ax_sin_sampled, self.canvas_sin_sampled = self.initialize_graph('Sampled Sinosoidal','t','x(t)')

        self.canvas_int.get_tk_widget().grid(column=8, row=0,columnspan=4)
        self.canvas_sin.get_tk_widget().grid(column=0, row=0,columnspan=4)
        self.canvas_sin_sampled.get_tk_widget().grid(column=4, row=0,columnspan=4)

        filename_label.grid(column=0, row=1,sticky=(W, E))
        filename_entry.grid(column=1, row=1, columnspan=3, sticky=(W, E))

        label = ttk.Label(self.frame,text="Please select type:")
        label.grid(column=0, row=3,columnspan=2,sticky=(W, E))
        self.selected_type = StringVar(value=Type.SIN.name)
        type_cb = ttk.Combobox(self.frame, textvariable=self.selected_type)
        type_cb['values'] = [Type.SIN.name,Type.COS.name]
        # prevent user typing a value
        type_cb['state'] = 'readonly'
        type_cb.grid(column=1, row=3,sticky=(W, E))

        self.amplitude = IntVar()
        amplitude_label = ttk.Label(self.frame, text="Amplitude")
        amplitude_label.grid(column=0, row=5,columnspan=2,sticky=(W, E))
        amplitude_input = ttk.Entry(self.frame, textvariable=self.amplitude)
        amplitude_input.insert(1, 1)

        amplitude_input.grid(column=0, row=6, columnspan=1,sticky=(N, W, E, S))

        self.freq = IntVar()
        freq_label = ttk.Label(self.frame, text="Frequency")
        freq_label.grid(column=1, row=5,columnspan=2,sticky=(W, E))
        freq_input = ttk.Entry(self.frame, textvariable=self.freq)
        freq_input.insert(1, 1)

        freq_input.grid(column=1, row=6, columnspan=1, sticky=(W, E))

        self.shifted = DoubleVar()
        shifted_label = ttk.Label(self.frame, text="Shifted By")
        shifted_label.grid(column=2, row=5,columnspan=2,sticky=(W, E))
        shifted_input = ttk.Entry(self.frame, textvariable=self.shifted)
        shifted_input.grid(column=2, row=6, columnspan=1,sticky=(N, W, E, S))

        generate_btn = ttk.Button(self.frame, text="Generate SIN / COS",command=self.on_click_generate)
        generate_btn.grid(column=0, row=7,columnspan=3,sticky=(W, E))
        save_sin_output=ttk.Button(self.frame,text="Save Sampled Sinosoidal",command=lambda: self.saveOutput(self.Sin,filename_entry.get()),bootstyle=(SUCCESS,OUTLINE))

        label = ttk.Label(self.frame,text="F_s")
        label.grid(column=0, row=8,columnspan=1,sticky=(W, E))
        self.fs= IntVar()
        fs_input = ttk.Entry(self.frame, textvariable=self.fs)
        fs_input.grid(column=1, row=8, columnspan=1,sticky=(N, W, E, S))
        sampling_btn = ttk.Button(self.frame, text=f"Sampling {self.selected_type.get()} Wave",command=self.on_click_Sampling)
        sampling_btn.grid(column=0, row=9,columnspan=3,sticky=(W, E))
        save_sin_output.grid(column=0, row=10,columnspan=4,sticky=(W, E))
        read_input.grid(column=8,row=1,columnspan=2,sticky=(W, E))
        interpolate_input.grid(column=10,row=1,columnspan=2,sticky=(W, E))
        save_interpolation_output.grid(column=8,row=2,columnspan=2,sticky=(W, E))
        clear__interpolation_output.grid(column=10,row=2,columnspan=2,sticky=(W, E))

    def on_click_generate(self):
        t,x_t = GenerateSinCos.generate_sin_cos(Type[self.selected_type.get()],self.amplitude.get(),self.freq.get(),self.shifted.get())
        signal = Signal(t,x_t)
        continous_out = signal
        self.plot_continous_graph(self.ax_sin,self.canvas_sin,signal,f"{self.selected_type.get()} Signal")

    def on_click_Sampling(self):
        if self.fs.get() < 2*self.freq.get():
            show_message_box("ERROR" , f"fs must be at least {2*self.freq.get()} ")
        n,x_n = GenerateSinCos.sampling_sin_cos(Type[self.selected_type.get()],self.amplitude.get(),self.freq.get(),self.shifted.get(),self.fs.get())
        signal = Signal(n,x_n)
        self.Sin=signal
        continous_out = signal
        self.plot_discrete_graph(self.ax_sin_sampled,self.canvas_sin_sampled,signal,f"Sampling {self.selected_type.get()} Signal")



