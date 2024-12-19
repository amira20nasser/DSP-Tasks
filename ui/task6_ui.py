from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from ui.ui_widgets import Tab  
from utils import *
from logic.basic_signal_operations import Signal
from logic.correlation import Correlation
from visualizer import *
from file_manpulator import *
from task6_test.CompareSignal import Compare_Signals
class Task6UI(Tab):
    def initialize_ui_variables(self):
        self.out = None
        self.a_signal = None
        self.b_signal = None
        self.save_file = StringVar()
        self.fs = IntVar()
        self.fs.set(100)
        self.file_manpulator = FileManpulator()
        self.input_visualizer = Visualizer(frame=self.frame,title='Input Signal(s)',xlabel='t',ylabel='x(t)')
        self.output_visualizer = Visualizer(frame=self.frame,title='Output Signal',xlabel='t',ylabel='x(t)')

    def __init__(self, notebook, name):
        super().__init__(notebook, name)
        self.initialize_ui_variables()

        input_label = ttk.Label(self.frame, text="Input signals:")
        sig_A_btn= ttk.Button(self.frame,text="Signal A", command=self.on_click_upload_sig_a,bootstyle=SUCCESS)
        sig_B_btn= ttk.Button(self.frame,text="Signal B",command=self.on_click_upload_sig_b,bootstyle=SUCCESS)
        fs_label = ttk.Label(self.frame, text="Fs:")
        fs_entry = ttk.Entry(self.frame, textvariable=self.fs)

        save_output=ttk.Button(self.frame,text="Save Output Signal",command=self.on_click_save_signal,bootstyle=(SUCCESS,OUTLINE))
        clear_output=ttk.Button(self.frame,text="Clear Output",command=self.on_click_clear,bootstyle=(SUCCESS,OUTLINE))
        filename_label = ttk.Label(self.frame, text="Save file name:")
        
        filename_entry = ttk.Entry(self.frame, textvariable=self.save_file)
        self.frame.grid(column=0, row=0,sticky=(W, E))
        input_label.grid(column=0, row=1,sticky=(W, E))
        sig_A_btn.grid(column=0, row=2,columnspan=2,sticky=(W, E))
        sig_B_btn.grid(column=2, row=2,columnspan=2,sticky=(W, E))


        correlation = ttk.Button(self.frame, text="Calculate Correlation",command=self.on_click_correlation,bootstyle=OUTLINE)
        test_correlation= ttk.Button(self.frame, text="Test Correlation",command=self.on_click_test_correlation)
        delay = ttk.Button(self.frame, text="Calculate Delay",command=self.on_click_calculate_delay)
        classify = ttk.Button(self.frame, text="Classify Signal",command=self.on_click_classify_signal)


        fs_label.grid(column=0, row=3,columnspan=1,sticky=(W, E))
        fs_entry.grid(column=1, row=3,columnspan=3,sticky=(W, E))

        correlation.grid(column=0,row=4,columnspan=2, sticky=(N, W, E, S))
        test_correlation.grid(column=2,row=4,columnspan=2, sticky=(N, W, E, S))
        delay.grid(column=0,row=5,columnspan=4, sticky=(N, W, E, S))
        classify.grid(column=0,row=6,columnspan=4, sticky=(N, W, E, S))

        self.input_visualizer.canvas.get_tk_widget().grid(column=0, row=0,columnspan=4)
        self.output_visualizer.canvas.get_tk_widget().grid(column=4, row=0,columnspan=4)

        filename_label.grid(column=4, row=1,sticky=(W, E))
        filename_entry.grid(column=5, row=1, columnspan=3, sticky=(W, E))
        save_output.grid(column=4,row=2,columnspan=4, sticky=(N, W, E, S))
        clear_output.grid(column=4,row=3,columnspan=4, sticky=(N, W, E, S))
       
    
    def on_click_clear(self):
        self.output_visualizer.clear_plotting()

    def on_click_upload_sig_a(self):
       self.input_visualizer.clear_plotting()
       x,y =  self.file_manpulator.loadSignal()
       self.a_signal = Signal(x,y)
       self.input_visualizer.plot_discrete_graph(signal=self.a_signal)

    def on_click_upload_sig_b(self):
       x,y =  self.file_manpulator.loadSignal()
       self.b_signal = Signal(x,y)
       self.input_visualizer.plot_discrete_graph(signal=self.b_signal)   

    def on_click_save_signal(self):
        self.file_manpulator.saveOutput(signal=self.out,file=self.save_file.get())

    def on_click_correlation(self):
        if self.a_signal==None or self.b_signal==None:
            show_message_box("DSP" , "Please upload signals A and B")
            return -1
        self.out = Correlation.correlate(self.a_signal,self.b_signal)
        self.output_visualizer.clear_plotting()
        self.output_visualizer.plot_discrete_graph(self.out)


    def on_click_test_correlation(self):
       self.input_visualizer.clear_plotting()

       x,y =  self.file_manpulator.loadSignal("task6_test/Point1 Correlation/Corr_input signal1.txt")
       self.a_signal = Signal(x,y)

       self.input_visualizer.plot_discrete_graph(signal=self.a_signal)

       x,y =  self.file_manpulator.loadSignal("task6_test/Point1 Correlation/Corr_input signal2.txt")
       self.b_signal = Signal(x,y)
       self.input_visualizer.plot_discrete_graph(signal=self.b_signal)   

       self.on_click_correlation()

       print(f"Result x: {self.out.x}")
       print(f"Result y: {self.out.y}")
       Compare_Signals("task6_test/Point1 Correlation/CorrOutput.txt",self.out.x,self.out.y)

    def on_click_calculate_delay(self):
        self.input_visualizer.clear_plotting()

        x,y =  self.file_manpulator.loadSignal("task6_test/Point2 Time analysis/TD_input signal1.txt")
        self.a_signal = Signal(x,y)
        self.input_visualizer.plot_discrete_graph(signal=self.a_signal)

        x,y =  self.file_manpulator.loadSignal("task6_test/Point2 Time analysis/TD_input signal2.txt")
        self.b_signal = Signal(x,y)
        self.input_visualizer.plot_discrete_graph(signal=self.b_signal)

        delay, self.out = Correlation.calculate_delay(self.a_signal,self.b_signal, self.fs.get())
        print(f"Delay:{delay} seconds")
        self.output_visualizer.clear_plotting()
        self.output_visualizer.plot_discrete_graph(self.out)
    
    def on_click_classify_signal(self):
        down = []
        down_path="task6_test/point3 Files/Class 1"
        for f in os.listdir(down_path):
            x, y = self.file_manpulator.loadSignalY(file=f"{down_path}/{f}")
            down.append(Signal(x,y))
        print(f"Loaded down: {len(down)} signals")
        
        up = []
        up_path="task6_test/point3 Files/Class 2"
        for f in os.listdir(up_path):
            x, y = self.file_manpulator.loadSignalY(file=f"{up_path}/{f}")
            up.append(Signal(x,y))
        print(f"Loaded up: {len(up)} signals")

        self.input_visualizer.clear_plotting()
        self.output_visualizer.clear_plotting()

        print("TEST CASE 1")
        x, y =  self.file_manpulator.loadSignalY("task6_test/point3 Files/Test Signals/Test1.txt")
        self.a_signal = Signal(x,y)
        Correlation.classify_signal(self.a_signal,down,up)
      
        self.output_visualizer.clear_plotting()
        self.input_visualizer.clear_plotting()
        self.input_visualizer.plot_discrete_graph(signal=self.a_signal)

        input("Press Enter to continue...")



        print("TEST CASE 2")
        x, y =  self.file_manpulator.loadSignalY("task6_test/point3 Files/Test Signals/Test2.txt")
        self.a_signal = Signal(x,y)
        Correlation.classify_signal(self.a_signal,down,up)

        self.output_visualizer.clear_plotting()
        self.input_visualizer.clear_plotting()
        self.input_visualizer.plot_discrete_graph(signal=self.a_signal)

        input("Testing done!")