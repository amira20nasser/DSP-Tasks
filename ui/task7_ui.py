from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.ui_widgets import Tab  
from logic.filters import *
from logic.basic_signal_operations import Signal
from utils import *
from visualizer import *
from file_manpulator import *
from logic.filters import *
from CompareSignal import *

class Task7UI(Tab):
    def initialize_ui_variables(self):
        self.input = None
        self.output = None
        self.save_file = StringVar()
        self.file_manpulator = FileManpulator()
        self.selected_type = StringVar(value=Type.LOW_PASS.value)
        self.input_visualizer = Visualizer(frame=self.frame,title='Input Signal',xlabel='t',ylabel='x(t)')
        self.output_visualizer = Visualizer(frame=self.frame,title='Filtered Signal',xlabel='t',ylabel='x(t)')

    def __init__(self, notebook, name):
        super().__init__(notebook, name)
        self.initialize_ui_variables()

        read_input= ttk.Button(self.frame,text="Read Signal", command=self.on_click_upload_sig,bootstyle=(SUCCESS))
        apply_filter= ttk.Button(self.frame,text="Apply Filter",command=self.on_click_apply_filter)
    
        save_output=ttk.Button(self.frame,text="Save Output",command=lambda:self.on_click_save_signal(self.output),bootstyle=(SUCCESS,OUTLINE))
        clear_output=ttk.Button(self.frame,text="Clear Output",command=self.output_visualizer.clear_plotting,bootstyle=(SUCCESS,OUTLINE))
        filename_label = ttk.Label(self.frame, text="Save file name:")
        filename_entry = ttk.Entry(self.frame, textvariable=self.save_file)
        self.frame.grid(column=0, row=0,sticky=(W, E))

        self.input_visualizer.canvas.get_tk_widget().grid(column=0, row=0,columnspan=4)
        self.output_visualizer.canvas.get_tk_widget().grid(column=4, row=0,columnspan=4)

        filename_label.grid(column=4, row=1,sticky=(W, E))
        filename_entry.grid(column=5, row=1, columnspan=3, sticky=(W, E))

        label = ttk.Label(self.frame,text="Please select type:")
        label.grid(column=0, row=2,columnspan=2,sticky=(W, E))
        type_cb = ttk.Combobox(self.frame, textvariable=self.selected_type)
        type_cb['values'] = [Type.LOW_PASS.value,Type.HIGH_PASS.value,Type.BAND_PASS.value,Type.BAND_REJECT.value]
        # prevent user typing a value
        type_cb['state'] = 'readonly'
        type_cb.grid(column=1, row=2,sticky=(W, E),columnspan=3)


        read_input.grid(column=0,row=1,columnspan=2,sticky=(W, E))
        apply_filter.grid(column=2,row=1,columnspan=2,sticky=(W, E))
        save_output.grid(column=4,row=2,columnspan=2,sticky=(W, E))
        clear_output.grid(column=6,row=2,columnspan=2,sticky=(W, E))

        self.sample_freq = IntVar(value=8000)
        fs_label = ttk.Label(self.frame, text="Value of sample_freq:")
        fs_input = ttk.Entry(self.frame, textvariable=self.sample_freq)
        fs_label.grid(column=0, row=3,columnspan=2,sticky=(W, E))
        fs_input.grid(column=1, row=3,sticky=(W, E),columnspan=3)
    
        self.cutoff_freq = IntVar(value=1500)
        fc_label = ttk.Label(self.frame, text="Value of cutoff_freq:")
        fc_input = ttk.Entry(self.frame, textvariable=self.cutoff_freq)
        fc_label.grid(column=4, row=3,columnspan=2,sticky=(W, E))
        fc_input.grid(column=6, row=3,columnspan=2,sticky=(W, E))
    
        self.StopBandAttenuation = IntVar(value=50)
        sba_label = ttk.Label(self.frame, text="StopBandAttenuation:")
        sba_input = ttk.Entry(self.frame, textvariable=self.StopBandAttenuation)
        sba_label.grid(column=0, row=4,columnspan=2,sticky=(W, E))
        sba_input.grid(column=1, row=4,sticky=(W, E),columnspan=3)
    
        self.TransitionBand = IntVar(value=500)
        tb_label = ttk.Label(self.frame, text="Value of TransitionBand(width):")
        tb_input = ttk.Entry(self.frame, textvariable=self.TransitionBand)
        tb_label.grid(column=4, row=4,columnspan=2,sticky=(W, E))
        tb_input.grid(column=6, row=4,columnspan=2,sticky=(W, E))
    
    def on_click_upload_sig(self):
       x,y =  self.file_manpulator.loadSignal()
       self.input_signal = Signal(x,y)
       self.input_visualizer.plot_discrete_graph(signal=self.input_signal)

    def on_click_apply_filter(self):
        # myfilter = LowPassFilter(fc1=1500,fs = 8000,transition_width=500)
        # window = HammingWindow(8000,500)
        # x,y = create_FIR( myfilter,window  )
        # Compare_Signals("task7_test\Testcase 1\LPFCoefficients.txt",x,y)
        # x,y= self.file_manpulator.loadSignal(file="task7_test\Testcase 2\ecg_low_pass_filtered.txt")
        # self.input_signal = Signal(x,y)
        # con_signal = conv_direct_method(Signal(x,y),self.input_signal)
        # Compare_Signals("task7_test\Testcase 2\ecg_low_pass_filtered.txt",con_signal.x,con_signal.y)
        
        # myfilter = HighPassFilter(fc1=1500,fs = 8000,transition_width=500)
        # window = BlackmanWindow(8000,500)
        # x_filter,y_filter = create_FIR( myfilter,window  )
        # Compare_Signals("task7_test\Testcase 3\HPFCoefficients.txt", x_filter,y_filter)
        # x,y = self.file_manpulator.loadSignal(file="task7_test\Testcase 4\ecg400.txt")
        # self.input_signal = Signal(x,y)
        # con_signal = conv_direct_method(Signal(x_filter,y_filter),self.input_signal)
        # Compare_Signals("task7_test\Testcase 4\ecg_high_pass_filtered.txt",con_signal.x,con_signal.y)

        mfilter = BandPassFilter(fc1=150,fc2=250,fs = 1000,transition_width=50)
        window = BlackmanWindow(fs=1000,transition_width=50)
        x,y = create_FIR( mfilter,window  )
        Compare_Signals("task7_test\Testcase 5\BPFCoefficients.txt",x,y)
        x,y = self.file_manpulator.loadSignal(file="task7_test\Testcase 6\ecg400.txt")
        self.input_signal = Signal(x,y)
        con_signal = conv_direct_method(Signal(x,y),self.input_signal)
        Compare_Signals("task7_test\Testcase 6\ecg_band_pass_filtered.txt",con_signal.x,con_signal.y)

        # mfilter = BandStopFilter(fc1=150,fs=1000,fc2=250,transition_width=50)
        # window = BlackmanWindow(fs=1000,transition_width=50)
        # x,y = create_FIR( mfilter,window  )
        # Compare_Signals("task7_test\Testcase 7\BSFCoefficients.txt",x,y)
        # t= self.selected_type.get()
        # myfilter = self.create_filter_obj(t)
        # stopbandattenuation =self.StopBandAttenuation.get()
        # window = self.create_window(stopbandattenuation)
        # # print(window.fs)
        # window = HanningWindow(
        #         fs=self.sample_freq.get(),
        #         transition_width=self.TransitionBand.get(),
        #     )
        # x,y = create_FIR( myfilter,window )
        # Compare_Signals("task7_test\Testcase 1\LPFCoefficients.txt",x,y)
        # con_signal = conv_direct_method(Signal(x,y),self.input_signal)
        # # con_signal = conv_fast_method(Signal(x,y),self.input_signal,self.sample_freq.get())

        # self.input_visualizer.plot_discrete_graph(signal=con_signal)
        # Compare_Signals("task7_test\Testcase 2\ecg_low_pass_filtered.txt",con_signal.x,con_signal.y)



    def on_click_save_signal(self,signal):
        self.file_manpulator.saveOutput( signal,self.save_file.get())

    def create_window(self,stopBandAttenuation):
        # print("in crerate window")
        # print(stopBandAttenuation)
        win =BlackmanWindow(
                fs=self.sample_freq.get(),
                transition_width=self.TransitionBand.get(),
            )
        if stopBandAttenuation >=74:
            win = BlackmanWindow(
                fs=self.sample_freq.get(),
                transition_width=self.TransitionBand.get(),
            )
        elif stopBandAttenuation >=53:
            win = HammingWindow(
                fs=self.sample_freq.get(),
                transition_width=self.TransitionBand.get(),
            ),
        elif stopBandAttenuation>=44:
            win = HanningWindow(
                fs = self.sample_freq.get(),
                transition_width=self.TransitionBand.get(),
            ),
        elif stopBandAttenuation>=20:
            win = RectangleWindow(
                fs = self.sample_freq.get(),
                transition_width=self.TransitionBand.get(),
            )
        else:
            messagebox.showerror("EROR", "Invalid stop band attenuation")
            win = None
        return win

    def create_filter_obj(self,typef):
        myfilter = None
        if typef == Type.LOW_PASS.value:
            myfilter = LowPassFilter(
                fc1=self.cutoff_freq.get(),
                fs = self.sample_freq.get(),
                transition_width=self.TransitionBand.get(),
            )
        elif typef == Type.HIGH_PASS.value:
            myfilter = HighPassFilter(
                fc1=self.cutoff_freq.get(),
                fs = self.sample_freq.get(),
                transition_width=self.TransitionBand
            )
        elif typef == Type.BAND_PASS.value:
            myfilter = BandPassFilter(
                fc1=self.cutoff_freq.get().split(' ')[0],
                fc2=self.cutoff_freq.get().split(' ')[1],
                fs = self.sample_freq.get(),
                transition_width=self.TransitionBand.get(),
            )
        else:
            myfilter= BandStopFilter(
                fc1=self.cutoff_freq.get().split(' ')[0],
                fc2=self.cutoff_freq.get().split(' ')[1],
                fs = self.sample_freq.get(),
                transition_width=self.TransitionBand.get(),
            )
        return myfilter
