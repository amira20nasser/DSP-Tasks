import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from ui.ui_widgets import Tab  
from logic.generate_sin_cos import *
from logic.basic_signal_operations import Signal

class Task2UI(Tab):
    def __init__(self, notebook, name):
        super().__init__(notebook, name)
        self.continous_out = None
        self.discrete_out = None
        
        self.ax_in.plot(np.random.rand(3,),np.zeros(3))
        self.canvas_in.draw()

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
        generate_btn.grid(column=1, row=7,sticky=(W, E))

    def on_click_generate(self):
        t,x_t = GenerateSinCos.generate(Type[self.selected_type.get()],self.amplitude.get(),self.freq.get(),self.shifted.get())
        signal = Signal(t,x_t)
        continous_out = signal
        self.plot_continous_graph(self.ax_in,self.canvas_in,signal,f"{self.selected_type.get()} Signal")

    def plot_continous_graph(self,ax,canvas,signal,title):
        ax.set_title(title)
        ax.plot(signal.x, signal.y),
        canvas.draw()

    def add(self):
        super().add()  
