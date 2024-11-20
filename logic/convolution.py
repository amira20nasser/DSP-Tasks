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
        x_shifted,y_shifted = Signal.shift_signal(original_signal,-1)
        
        x_new , y_new = Signal.subtract_signals(original_signal,Signal(x_shifted,y_shifted))
       
        first_derivative = Signal(x_new,y_new)
        x_shifted1,y_shifted1 = Signal.shift_signal(original_signal,1)
        
        x_new_sec , y_new_sec = Signal.subtract_signals(Signal(x_shifted1,y_shifted1),original_signal)
    
        x_final , y_final = Signal.subtract_signals(Signal(x_new_sec , y_new_sec) , first_derivative )
       
        second_derivative = Signal(x_final,y_final)
        
        first_derivative.x = np.arange(0,len(original_signal.x)-1)
        first_derivative.y = y_new[1:len(first_derivative.x)+1]

        second_derivative.x = np.arange(0,len(first_derivative.x)-1)
        second_derivative.y = y_final[2:len(second_derivative.x)+2]
        print("FIRST DERIVATIVE")
        print(f"X={first_derivative.x},Shape{first_derivative.x.shape}")
        print(f"Y={first_derivative.y},shape{first_derivative.y.shape}")
        print("SECOND DERIVATIVE")
        print(f"X={second_derivative.x},shape{second_derivative.x.shape}")
        print(f"Y={second_derivative.y},shape{second_derivative.y.shape}")
        return first_derivative,second_derivative
    
    @staticmethod
    def convolve(signal_1,signal_2):
        len_1 =len(signal_1.x)
        len_2  = len(signal_2.x)

        L = len_1+len_2-1
        y_result = np.zeros(L)

        x_start = signal_1.x[0] + signal_2.x[0]
        x_end = x_start + L - 1
        
        x_result = np.arange(x_start,x_end+1)

        for i in range(len_1):
            for j in range(len_2):
                y_result[i+j] += signal_1.y[i] * signal_2.y[j]

        print("len y ",len(y_result))
        print(y_result)

        print("len x ",len(x_result))
        print(x_result)
        
        singal = Signal(x_result,y_result)
        return singal

        print()

















    # y(n)=k=0∑M−1 (x(k)⋅h(n−k))