import os
import numpy as np
from tkinter import messagebox
from tkinter import filedialog

class FileManpulator:
    def __init__(self):
        self.file = None
        
    def loadSignal(self,file=None):
        if file is None:
            self.file=filedialog.askopenfilename(initialdir = os.path.expanduser( os.getcwd()),title = "Select a text file containing the signal B.",filetypes = (("Text files","*.txt"), ("all files","*.*")))
        else:
            self.file=file
        x,y = np.loadtxt(self.file, dtype=float, skiprows=3, delimiter=" ", unpack=True)  
        return x,y
    
    def saveOutput(self, signal,file):
        if signal == None:
            messagebox.showerror("DSP" , "No output signal to save")
        elif not file :
            messagebox.showerror("DSP" , "Please enter save file name")
        else:
            print("Saved points X:",signal.x)
            print("Saved points y:",signal.y)
            output=np.stack((signal.x,signal.y),axis=1)
            np.savetxt(fname=file+'.txt',header='0\n0\n'+str(len(signal.x)), comments='', delimiter=' ', X=output)
            messagebox.showinfo("DSP" , "Signal saved successfully")   