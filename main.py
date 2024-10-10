
from ui.ui_widgets import UI
from ui.task1_ui import Task1UI
from ui.task2_ui import Task2UI

def main():
    ui = UI()
    root, notebook = ui.initialize()

    task1_tab = Task1UI(notebook, "Task 1")
    task1_tab.add()

    task2_tab = Task2UI(notebook, "Task 2")
    task2_tab.add()

    root.mainloop()

main()







# from tkinter import *
# from tkinter import ttk
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# class UI:
#     def initialize(self):
#         root = Tk()
#         root.title("Digital Signal Processing")
#         root.columnconfigure(0, weight=1)
#         root.rowconfigure(0, weight=1)

#         notebook = ttk.Notebook(root)
#         notebook.grid(column=0, row=0, sticky=(N, W, E, S))  # Use grid for notebook
#         return root, notebook

#     def loadSignal(file):
#         return 0

#     def displaySignal(file):
#         return 0

# class Tab:
# #Task 1
#     def __init__(self,notebook,name):
#         self.notebook=notebook
#         self.name=name
#         self.frame = ttk.Frame(notebook,padding="3 3 12 12")
#         sig_A= ttk.Button(self.frame,text="Signal A")
#         sig_B= ttk.Button(self.frame,text="Signal B")
#         fig = plt.Figure(figsize=(4, 3), dpi=100)
#         ax = fig.add_subplot(111)
#         canvas =  FigureCanvasTkAgg(fig, master=self.frame)
#         canvas.draw()
#         display=ttk.Button(self.frame,text="Display Signal")

#         self.frame.grid(column=0, row=0,sticky=(W, E))
#         sig_A.grid(column=0, row=0,columnspan=2,sticky=(W, E))
#         sig_B.grid(column=2, row=0,columnspan=2,sticky=(W, E))
#         canvas.get_tk_widget().grid(column=0, row=3,columnspan=4)

#         display.grid(column=0,row=4,columnspan=4, sticky=(N, W, E, S))
       
#     def add(self):
#         for child in self.frame.winfo_children(): 
#             child.grid_configure(padx=5, pady=5)
#         notebook.add(self.frame, text=self.name)

# class Task1(Tab):
#     def __init__(self,notebook,name):
#         super().__init__(notebook,name)
#         AplusB= ttk.Button(self.frame,text="A + B")
#         AminusB= ttk.Button(self.frame,text="A - B")
#         AtimesB= ttk.Button(self.frame,text="A × B")
#         AmulC= ttk.Button(self.frame,text="c × A")
#         c_label=ttk.Label(self.frame,text="Value of c:")
#         c=StringVar()
#         c_input=ttk.Entry(self.frame,textvariable=c)

#         AplusB.grid(column=0, row=5)
#         AminusB.grid(column=1, row=5)
#         AtimesB.grid(column=2, row=5)
#         AmulC.grid(column=3, row=5)
#         c_label.grid(column=0,row=6)
#         c_input.grid(column=1,row=6,columnspan=3,sticky=(W, E))

#     def addSignals(signal_a,signal_b):
#         return 0

#     def subtractSignals(signal_a,signal_b):
#         return 0

#     def multiplySignals(signal_a,signal_b):
#         return 0

#     def scaleSignal(signal):
#         return 0
        
#     def divideSignals(signal_a,signal_b):
#         return 0

# class Task2(Tab):
#     def init(self,notebook,name):
#         super().__init__(notebook,name)  # second page

# ui=UI()
# root,notebook = ui.initialize()
# t1=Task1(notebook, "Task 1")
# t1.add()
# t2= Task2(notebook, 'Task-2')
# t2.add()
# root.mainloop()

