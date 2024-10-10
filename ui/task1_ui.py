from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from ui.ui_widgets import Tab  
from utils import *
from logic.basic_signal_operations import *

class Task1UI(Tab):
    def __init__(self, notebook, name):
        super().__init__(notebook, name)
        # A = load_signal()
        # B = load_signal()
        AplusB = ttk.Button(self.frame, text="A + B",command=lambda: BasicSignalOperations.add_signals(signal_a=0,signal_b=0),)
        AminusB = ttk.Button(self.frame, text="A - B",command=lambda: BasicSignalOperations.subtract_signals(signal_a=0,signal_b=0))
        AtimesB = ttk.Button(self.frame, text="A × B",command=lambda: BasicSignalOperations.multiply_signals(signal_a=0,signal_b=0))
        AmulC = ttk.Button(self.frame, text="c × A",command=lambda: BasicSignalOperations.scale_signal(signal=0, c=0))
        AdivideB = ttk.Button(self.frame, text="c / A",command=lambda: BasicSignalOperations.divide_signals(signal_a=0,signal_b=0))

        c_label = ttk.Label(self.frame, text="Value of c:")
        c = StringVar()
        c_input = ttk.Entry(self.frame, textvariable=c)

        AplusB.grid(column=0, row=5)
        AminusB.grid(column=1, row=5)
        AtimesB.grid(column=2, row=5)
        AmulC.grid(column=3, row=5)
        AdivideB.grid(column=4, row=5)

        c_label.grid(column=0, row=6)
        c_input.grid(column=1, row=6, columnspan=3, sticky=(W, E))

    def add(self):
        super().add()  
