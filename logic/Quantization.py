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
        intervals = np.arange(mn_value, mx_value+step+step, step)
        print(f"intervals {intervals}")
        midpoints=(intervals[:-1]+intervals[1:])/2
        print(f"midpoints {midpoints}")
        # return index of interval that belongs to 
        
        interval_index = np.digitize(np.clip(x_n,a_min=midpoints[0],a_max=midpoints[-1]), midpoints)
        print(f"index intervals{interval_index}")
        x_q = [np.round((midpoints[i - 1] + midpoints[i]) / 2,4) for i in interval_index]

        bits = int(np.log2(levels))
        encoded_index = [format(index-1,f'0{bits}b') for index in interval_index]
        print("ENCODED INDICIES")
        print(encoded_index)
        print("Quantized Sampled")
        print(x_q)
        return interval_index, x_q,encoded_index