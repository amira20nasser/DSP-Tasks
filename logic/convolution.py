import numpy as np
from logic.basic_signal_operations import *
class Convolution:
    @staticmethod
    def compute_average(original_signal,window_size):
        new_len = len(original_signal.x) - window_size + 1
        x = np.arange(0,new_len)
        y = []
        avg_signal  = Signal(x,y)
        print("new avg sig x",avg_signal.x)

        for i in range(len(original_signal.x)):
            if(new_len==0):
                break
            new_len-=1
            # print(original_signal.y[i:i+window_size])
            sm = np.round( sum(original_signal.y[i:i+window_size]) /window_size, 3)
            avg_signal.y.append(sm)
    
        print("new avg sig y",avg_signal.y)
        return avg_signal
    
    @staticmethod
    def sharpening_sig(original_signal):
        # Y(n) = x(n)-x(n-1) 
        # Y(n)= x(n+1)-2x(n)+x(n-1) 
        x_shifted,y_shifted = original_signal.shift_signal(original_signal,-1)
        x_new , y_new = original_signal.subtract_signals(original_signal,Signal(x_shifted,y_shifted))
        print("first driv x",x_new,"y",y_new)
        firt_drev = Signal(x_new,y_new)

        x_shifted1,y_shifted1 = original_signal.shift_signal(original_signal,1)
        x_new_sec , y_new_sec = original_signal.subtract_signals(Signal(x_shifted,y_shifted),original_signal)

        x_final , y_final = original_signal.subtract_signals(Signal(x_new_sec , y_new_sec) , firt_drev )
        second_derivative = Signal(x_final,y_final)
        print("second driv x",x_final,"y",y_final)

        return firt_drev,second_derivative
    
    def convolve():
        print()
    # y(n)=k=0∑M−1 (x(k)⋅h(n−k))