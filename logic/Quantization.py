import numpy as np 
from logic.basic_signal_operations import *

class Quatization:

    @staticmethod
    def quantize_signal(signal,levels):
        x_n = signal.y
        mx_value = max(x_n)
        mn_value = min(x_n)
        print(mx_value)
        print(mn_value)
        step = (mx_value - mn_value) / levels
        intervals = np.arange(mn_value, mx_value+step, step)
        print(intervals)
        # print(step)
        # ranges = [[mn_value,np.round(mn_value+step,3)]]
        # value = mn_value
        # for i in range(levels-1):
        #     value = np.round(value + step, 3)
        #     if (value+step > mx_value):
        #         ranges.append([value,mx_value])
        #         break
        #     ranges.append([value,np.round(value + step, 3)])
        # print(ranges)  
        # return index of interval that belong to 
        belong_interval = np.digitize(x_n, intervals)
        x_q = [(intervals[i - 1] + intervals[i]) / 2 for i in belong_interval]
        print(x_q)
        return belong_interval, x_q