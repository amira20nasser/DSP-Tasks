import numpy as np 

from logic.basic_signal_operations import *


class Quatization:

    @staticmethod
    def quantize_signal(signal,levels):
        x_n = signal.y
        mx_value = max(x_n)
        mn_value = min(x_n)
        print(f"max V->{mx_value}")
        print(f"min V->{mn_value}")
        print(f"#LEVELS->{levels}")
        step = np.round((mx_value - mn_value) / levels,4)
        print(f"Each step->{step}")
        intervals = np.arange(mn_value, mx_value+step, step)
        print(f"intervals {intervals}")
        x_n = np.clip(x_n, a_min=intervals[0], a_max=intervals[-1])
        print("X_n",x_n)
        # return index of interval that belongs to 
        interval_index = np.digitize(x_n, intervals,right=True)
        interval_index= [x if x >=1  else 1 for x in interval_index]
        # interval_index= [x if x <= levels  else levels for x in interval_index]
        print(f"index intervals{interval_index}")
        x_q = [np.round((intervals[i - 1] + intervals[i]) / 2,2)  for i in interval_index]
        bits = int(np.log2(levels))
        encoded_index = [format(index-1,f'0{bits}b') for index in interval_index]

        print("ENCODED INDICIES")
        print(encoded_index)
        print("Quantized Sampled")
        print(x_q)

        return interval_index, x_q,encoded_index
        
    @staticmethod
    def calculate_error(x_q,x_n):
        error = x_q - x_n
        print("Quantization Error")
        print(error)
        return error 
