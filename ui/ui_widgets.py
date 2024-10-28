import matplotlib
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import numpy as np
from logic.basic_signal_operations import Signal
from utils import show_message_box

class UI:
    def initialize(self):
        root = ttk.Window(themename='flatly')

        # Configure the style for all widgets
        root.title("Digital Signal Processing")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        notebook = ttk.Notebook(root,padding=5,bootstyle=SECONDARY)
        notebook.grid(column=0, row=0, sticky=(N, W, E, S))  # Use grid for notebook
        return root, notebook

class Tab:
    def __init__(self,notebook,name):
        matplotlib.style.use('seaborn-v0_8-pastel')

        self.notebook=notebook
        self.name=name
        self.frame = ttk.Frame(notebook,padding="3 3 12 12")

        
    def add(self):
        for child in self.frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        self.notebook.add(self.frame, text=self.name)






