from enum import Enum
import math 
import numpy as np 
from logic.convolution import *
from logic.basic_signal_operations import *
from logic.fourier_transform import *
from abc import ABC, abstractmethod

class Type(Enum):
    LOW_PASS = 'Low Pass'
    HIGH_PASS = 'High Pass'
    BAND_PASS = 'Band Pass'
    BAND_REJECT = 'Band Reject'

class Filter(ABC):
    def __init__(self,fc1,fs,transition_width):
        self.fc1 = fc1
        self.norm_fc1 = fc1 / fs

    @abstractmethod
    def compute_point(self,n):
        pass

class LowPassFilter(Filter):
    def __init__(self,fc1,fs,transition_width):
        super().__init__(fc1,fs,transition_width)
        self.fc1_dash_norm = (self.fc1 + (transition_width/2))/fs

    def compute_point(self,n):
        if n == 0:
            return  2 * self.fc1_dash_norm
        else:
            return (2 * self.fc1_dash_norm) * (np.sin(n*2*math.pi*self.fc1_dash_norm)/(n*2*math.pi*self.fc1_dash_norm))

class HighPassFilter(Filter):
    def __init__(self,fc1,fs,transition_width):
        super().__init__(fc1,fs,transition_width)
        self.fc1_dash_norm = (self.fc1 - (transition_width/2))/fs

    def compute_point(self,n):
        if n == 0:
            return 1 - (2 * self.fc1_dash_norm)
        else:
            return (-2 * self.fc1_dash_norm) * (np.sin(n*2*math.pi*self.fc1_dash_norm)/(n*2*math.pi*self.fc1_dash_norm))


class BandPassFilter(Filter):
    def __init__(self,fc1,fs,transition_width,fc2):
        super().__init__(fc1,fs,transition_width)
        self.fc2 = fc2
        self.norm_fc2 = fc2 / fs
        self.fc1_dash_norm = (self.fc1 - (transition_width/2))/fs
        self.fc2_dash_norm = (self.fc2 + (transition_width/2))/fs

    def compute_point(self,n):
        if n==0:
            return 2 * (self.fc2_dash_norm - self.fc1_dash_norm)
        else:
            factor1  = (2 * self.fc1_dash_norm) * (math.sin(n*2*math.pi*self.fc1_dash_norm)/(n*2*math.pi*self.fc1_dash_norm))
            factor2  = (2 * self.fc2_dash_norm) * (math.sin(n*2*math.pi*self.fc2_dash_norm)/(n*2*math.pi*self.fc2_dash_norm))
            return factor2  - factor1 

class BandStopFilter(Filter):
    def __init__(self,fc1,fs,transition_width,fc2):
        super().__init__(fc1,fs,transition_width)
        self.fc2 = fc2
        self.norm_fc2 = fc2 / fs
        self.fc1_dash_norm = (self.fc1 + (transition_width/2)) / fs
        self.fc2_dash_norm = (self.fc2 - (transition_width/2)) / fs

    def compute_point(self,n):
        if n==0:
            return 1 - (2 * (self.fc2_dash_norm - self.fc1_dash_norm))
        else:
            first_term = (2 * self.fc1_dash_norm) * (math.sin(n*2*math.pi*self.fc1_dash_norm)/(n*2*math.pi*self.fc1_dash_norm))
            second_term = (2 * self.fc2_dash_norm) * (math.sin(n*2*math.pi*self.fc2_dash_norm)/(n*2*math.pi*self.fc2_dash_norm))
            return first_term - second_term

class Window(ABC):
    def __init__(self,fs,transition_width):
        self.fs = fs
        self.transition_width = transition_width
        self.N = self.calculate_window_length()

    def calculate_window_length(self):
        transition_width_norm = self.transition_width / self.fs
        n = np.ceil(self.get_normalization_factor() / transition_width_norm)
        return int(n + 1) if n % 2 == 0 else int(n)

    @abstractmethod
    def get_normalization_factor(self):
        pass

    @abstractmethod
    def compute_window_function(self):
        pass

class RectangleWindow(Window):
    def get_normalization_factor(self):
        return 0.9

    def compute_window_function(self):
        fromV = (self.N-1) /2
        x = np.arange(-fromV , fromV+1)   
        y = np.ones(self.N)
        return x,y

class HanningWindow(Window):
    def get_normalization_factor(self):
        return 3.1

    def compute_window_function(self):
        fromV = (self.N-1) /2
        x = np.arange(-fromV , fromV+1)
        y = 0.5+0.5*np.cos((2*math.pi*x)/self.N)
        return x,y

class HammingWindow(Window):
    def get_normalization_factor(self):
        return 3.3

    def compute_window_function(self):
        fromV = (self.N-1)/2
        
        x = np.arange(-fromV , fromV+1)
        y = 0.54+0.46*np.cos((2*math.pi*x)/self.N)
        return x,y

class BlackmanWindow(Window):
    def get_normalization_factor(self):
        return 5.5

    def compute_window_function(self):
        fromV = (self.N-1) /2
        x = np.arange(-fromV , fromV+1)    
        middle = 0.5*np.cos((2*math.pi*x)/(self.N-1))
        last = 0.08*np.cos((4*math.pi*x)/(self.N-1))
        y = 0.42 + middle + last
        return x,y


def create_FIR(mfilter,window):
    y_filter = []
    n = window.N
    fromV = (n-1) /2
    x_filter = np.arange(-fromV , fromV+1)
    for i in x_filter:
        y_filter.append(mfilter.compute_point(i))
    y_filter = np.array(y_filter)   

    x_win,y_win = window.compute_window_function()
    y_final = y_win*y_filter

    return x_filter,y_final


def conv_direct_method(signal1_obj,signal2_obj):
   signal_obj =  Convolution.convolve(signal1_obj,signal2_obj)
   print("direct->",len(signal_obj.y))
   return signal_obj

def conv_fast_method(signal1_obj,signal2_obj,fs):
    amplitude1, phase1 = FourierTransform.dtf_transform(signal1_obj.y,fs)
    amplitude2, phase2 =  FourierTransform.dtf_transform(signal2_obj.y,fs)
    amp = np.multiply(amplitude1 , amplitude2)
    phase = np.multiply(phase1 , phase2)
    X_n = FourierTransform.idtf_transform(amp,phase)
    indicies =[i for i in range(len(X_n))]
    print("conv using fast len ",len(X_n))
    return Signal(indicies,X_n)