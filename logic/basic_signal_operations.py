from utils import show_message_box
import numpy as np
class Signal:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @staticmethod
    def add_signals(A, B):
        union_set = sorted(set(A.x).union(set(B.x)))
        y_a = Signal.add_ranges(A.x,A.y,list(union_set))
        y_b = Signal.add_ranges(B.x,B.y, list(union_set))
        print(union_set)
        print(y_a)
        print(y_b)
        result_y = np.array(y_a) + np.array(y_b)
        print(union_set)
        print(result_y) 
        # new_signal = Signal(union_set,result_y)
        return union_set,result_y
    @staticmethod
    def subtract_signals(A, B):
        union_set = sorted(set(A.x).union(set(B.x)))
        print("signal A x",A.x)
        print("signal A y",A.y)
        y_a = Signal.add_ranges(A.x,A.y,list(union_set))
        y_b = Signal.add_ranges(B.x,B.y, list(union_set))
        print(union_set)
        print(y_a)
        print(y_b)
        result_y = np.array(y_a) + -1*np.array(y_b)
        print(union_set)
        print(result_y) 
        # new_signal = Signal(union_set,result_y)
        return union_set,result_y
    @staticmethod

    def fold_signal(A):
        res_y = []
        res_x=[]
        res_y = list(reversed(A.y))
        res_x = A.x
        print("FOLD X[",res_x)
        print("FOLD Y[",res_y)
        return res_x,res_y 

    @staticmethod
    def scale_signal(A, c):
        res_x=A.x
        res_y=A.y*c
        return res_x,res_y
    @staticmethod
    def shift_signal(A, c):
        res_x=A.x-c
        #res_y = [A.y[list(A.x).index(x)] for x in res_x if x in A.x ]
        print(res_x)
        print(A.y)
        return res_x,A.y
    # add missing values in x by making y = 0 
    @staticmethod
    def add_ranges(signal_indices,signal_samples, unioin):
        new_samples = [signal_samples[np.argmax(signal_indices == x)] if x in signal_indices else 0 for x in unioin]
        print(new_samples)
        return new_samples