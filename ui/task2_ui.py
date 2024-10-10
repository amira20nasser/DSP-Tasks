from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from ui.ui_widgets import Tab  # Assuming Tab class is in ui.py

class Task2UI(Tab):
    def __init__(self, notebook, name):
        super().__init__(notebook, name)

    def add(self):
        super().add()  
