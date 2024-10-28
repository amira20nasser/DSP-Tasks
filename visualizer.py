import numpy as np
from tkinter import messagebox
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from logic.basic_signal_operations import Signal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Visualizer:
    def __init__(self,frame,title,xlabel,ylabel):
        self.fig = plt.Figure(figsize=(5, 4))
        self.frame = frame
        self.title = title
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title(title)
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)

    def clear_plotting(self):
        self.ax.clear()
        self.canvas.draw()

    def plot_continous_graph(self,signal):
        self.ax.set_title(self.title)
        self.ax.plot(signal.x, signal.y),
        self.canvas.draw()

    def plot_discrete_graph(self,signal):
        line_colors = ['b-', 'r-', 'g-','m-']
        self.ax.set_title(self.title)
        self.ax.stem(signal.x, signal.y, linefmt=line_colors[np.random.randint(4)],markerfmt="o" , basefmt="k"),
        self.canvas.draw()
        
    def interpolate(self,signal):
        if signal==None:
            messagebox.showerror("DSP" , "Please upload signal to interpolate")

        f = interp1d(signal.x, signal.y, kind='cubic')
        xnew = np.arange(np.min(signal.x),np.max(signal.x),step=0.01)
        ynew = f(xnew)   # use interpolation function returned by `interp1d`
        self.Interpolation=Signal(xnew,ynew)
        self.ax.set_title('Input Signal Interpolated')
        self.ax.plot(signal.x, signal.y, 'o', xnew, ynew, '-')
        self.canvas.draw()