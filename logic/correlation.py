import os
import numpy as np
from math import sqrt
from logic.basic_signal_operations import *

class Correlation:
    @staticmethod
    def correlate(signal_a,signal_b):
        len_a = len(signal_a.x)
        len_b = len(signal_b.x)
        if len_a==len_b:
            L=len_a
        else:
            L = len_a + len_b - 1
        y_result = np.zeros(L)

        x_start = signal_a.x[0] + signal_b.x[0]
        x_end = x_start + L - 1
        
        x_result = np.arange(x_start,x_end+1,dtype=float)

        for i in range(L):
            norm_a=0
            norm_b=0
            for j in range(len_a):
                y_result[i] += signal_a.y[j] * signal_b.y[(j+i)%len_b]
                norm_a+= signal_a.y[j]**2
                norm_b+= signal_b.y[(j+i)%len_b]**2

            y_result[i]=y_result[i]/sqrt(norm_a*norm_b)

        # print("X:", x_result)
        
        # print("y:", y_result)

        signal = Signal(x_result,y_result)
        return signal

    @staticmethod
    def calculate_delay(signal_a,signal_b,fs):
        corr = Correlation.correlate(signal_a, signal_b)
        max_corr_idx = np.argmax(corr.y)
        delay = max_corr_idx / fs
        return delay, corr

    @staticmethod
    def classify_signal(signal,a,b):
        max_corr_a=[]
        for sig in a:
            corr = Correlation.correlate(signal, sig)
            max_corr_a.append(np.max(corr.y))
        avg_corr_a=np.array(max_corr_a).mean()

        max_corr_b=[]
        for sig in b:
            corr = Correlation.correlate(signal, sig)
            max_corr_b.append(np.max(corr.y))
        avg_corr_b=np.array(max_corr_b).mean()

        print(f"Class 1: {avg_corr_a}")
        print(f"Class 2: {avg_corr_b}")

        if avg_corr_a == avg_corr_b:
            print("Cannot be determined")
        elif avg_corr_a>avg_corr_b:
            print("Class 1")
        elif avg_corr_a<avg_corr_b:
            print("Class 2")










