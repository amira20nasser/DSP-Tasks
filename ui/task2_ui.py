import numpy as np
from tkinter import *
from tkinter import ttk
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
        sig_A= ttk.Button(self.frame,text="Read Input", command=lambda: self.loadSignal('A'))
        sig_B= ttk.Button(self.frame,text="Interpolate Input",command=lambda: self.interpolate(self.ax_in,self.canvas_in,self.A,''))
        self.continous_out = None
        self.discrete_out = None
        
        # self.ax_in.plot(np.random.rand(1000000,),np.zeros(1000000))
        # self.canvas_in.draw()

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
        amplitude_input.grid(column=0, row=6, columnspan=1,sticky=(N, W, E, S))

        self.freq = IntVar()
        freq_label = ttk.Label(self.frame, text="Frequency")
        freq_label.grid(column=1, row=5,columnspan=2,sticky=(W, E))
        freq_input = ttk.Entry(self.frame, textvariable=self.freq)
        freq_input.grid(column=1, row=6, columnspan=1, sticky=(W, E))

        self.shifted = DoubleVar()
        shifted_label = ttk.Label(self.frame, text="Shifted By")
        shifted_label.grid(column=2, row=5,columnspan=2,sticky=(W, E))
        shifted_input = ttk.Entry(self.frame, textvariable=self.shifted)
        shifted_input.grid(column=2, row=6, columnspan=1,sticky=(N, W, E, S))

        generate_btn = ttk.Button(self.frame, text="Generate SIN / COS",command=self.on_click_generate)
        generate_btn.grid(column=0, row=7,columnspan=3,sticky=(W, E))

        label = ttk.Label(self.frame,text="F_s")
        label.grid(column=0, row=8,columnspan=1,sticky=(W, E))
        self.fs= IntVar()
        fs_input = ttk.Entry(self.frame, textvariable=self.fs)
        fs_input.grid(column=1, row=8, columnspan=1,sticky=(N, W, E, S))
        sampling_btn = ttk.Button(self.frame, text=f"Sampling {self.selected_type.get()} Wave",command=self.on_click_Sampling)
        sampling_btn.grid(column=0, row=9,columnspan=3,sticky=(W, E))

    def on_click_generate(self):
        t,x_t = GenerateSinCos.generate_sin_cos(Type[self.selected_type.get()],self.amplitude.get(),self.freq.get(),self.shifted.get())
        signal = Signal(t,x_t)
        continous_out = signal
        self.plot_continous_graph(self.ax_out,self.canvas_out,signal,f"{self.selected_type.get()} Signal")

    def on_click_Sampling(self):
        if self.fs.get() < 2*self.freq.get():
            show_message_box("ERROR" , f"fs must be at least {2*self.freq.get()} ")
        n,x_n = GenerateSinCos.sampling_sin_cos(Type[self.selected_type.get()],self.amplitude.get(),self.freq.get(),self.shifted.get(),self.fs.get())
        signal = Signal(n,x_n)
        continous_out = signal
        self.plot_discrete_graph(self.ax_out,self.canvas_out,signal,f"Sampling {self.selected_type.get()} Signal")


    def plot_continous_graph(self,ax,canvas,signal,title):
        ax.set_title(title)
        ax.plot(signal.x, signal.y),
        canvas.draw()
    def interpolate(self,ax,canvas,signal,title):
        if self.A==None:
            show_message_box("DSP" , "Please upload signal A")
        f = interp1d(signal.x, signal.y, kind='cubic')
        xnew = np.arange(np.min(signal.x),np.max(signal.x),step=0.1)
        ynew = f(xnew)   # use interpolation function returned by `interp1d`
        ax.plot(signal.x, signal.y, 'o', xnew, ynew, '-')
        canvas.draw()

    def add(self):
        super().add()  
