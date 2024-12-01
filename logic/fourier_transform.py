import numpy as np
import math
import cmath
class FourierTransform:
    @staticmethod
    def dtf_transform(signal ,fs):
        print()
        # return amplitude and phaseshift 
       
    @staticmethod
    def idtf_transform(amplitude, phaseshift):
        x_n = []
        length = len(amplitude)
        for n in range(length): # n=0 
            sumk = complex(0,0)
            for k in range(length):
                adjacent = amplitude[k] * math.cos(phaseshift[k])
                opposite = amplitude[k] * math.sin(phaseshift[k])
                x_k = complex(adjacent,opposite)
                angle = (2 * math.pi * k * n) / length
                term = x_k * complex(math.cos(angle),math.sin(angle))
                sumk+= term
            x_n.append(sumk.real/length)

        return x_n
            




