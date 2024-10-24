import numpy as np
from enum import Enum

class Type(Enum):
    SIN ='SIN'
    COS ='COS'


class GenerateSinCos:
    @staticmethod
    def generate_sin_cos(sig_type : Type,amp,freq,shifted):
        # t = np.linspace(0, 2 * np.pi, 1) 
        t = np.arange(0, 1, 0.01)
        if sig_type == Type.SIN:
            x_t = amp *np.sin(2*np.pi*freq * t+shifted)
        elif sig_type == Type.COS:
             x_t = amp * np.cos(2*np.pi*freq * t+shifted)
        else:
            print("!!TYPE SIGNAL NOT SIN OR COS!!")
            t=0
            x_t = -1
        return t,x_t    

    @staticmethod
    def sampling_sin_cos(sig_type : Type,amp,freq,shifted,fs):
        n = np.arange(0, 1,1/fs) 
        if sig_type == Type.SIN:
            x_n = amp * np.sin(2* np.pi * freq *n )
        elif sig_type == Type.COS:
            x_n = amp * np.cos(2* np.pi * freq*n )
        else:
            print("!!SAMPLING TYPE SIGNAL NOT SIN OR COS!!")
            n=0
            x_n = -1
        print (n)
        print(x_n)
        return n,x_n        