from tkinter import *
from tkinter import ttk

def loadSignal(file):
    return 0
def displaySignal(file):
    return 0
def addSignals(signal_a,signal_b):
    return 0
def subtractSignals(signal_a,signal_b):
    return 0
def multiplySignals(signal_a,signal_b):
    return 0
def scaleSignal(signal):
    return 0
def divideSignals(signal_a,signal_b):
    return 0

root = Tk()
root.title("Digital Signal Processing")

notebook = ttk.Notebook(root)
notebook.grid(column=0, row=0, sticky=(N, W, E, S))  # Use grid for notebook

#Task 1

frame_1 = ttk.Frame(notebook,padding="3 3 12 12")
sig_A= ttk.Button(frame_1,text="Signal A")
sig_B= ttk.Button(frame_1,text="Signal B")
AplusB= ttk.Button(frame_1,text="A + B")
AminusB= ttk.Button(frame_1,text="A - B")
AtimesB= ttk.Button(frame_1,text="A × B")
AmulC= ttk.Button(frame_1,text="c × A")
c_label=ttk.Label(frame_1,text="Value of c:")
c=StringVar()
c_input=ttk.Entry(frame_1,textvariable=c)


frame_1.grid(column=0, row=0,sticky=(W, E))
sig_A.grid(column=0, row=0,columnspan=2,sticky=(W, E))
sig_B.grid(column=2, row=0,columnspan=2,sticky=(W, E))
AplusB.grid(column=0, row=1)
AminusB.grid(column=1, row=1)
AtimesB.grid(column=2, row=1)
AmulC.grid(column=3, row=1)

c_label.grid(column=0,row=2)

c_input.grid(column=1,row=2,columnspan=3,sticky=(W, E))

for child in frame_1.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

notebook.add(frame_1, text='Task 1')



f2 = ttk.Frame(notebook)   # second page

notebook.add(f2, text='Task 2')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
