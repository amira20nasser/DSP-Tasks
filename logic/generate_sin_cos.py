import numpy as np
from enum import Enum

class Type(Enum):
    SIN ='SIN'
    COS ='COS'


class GenerateSinCos:
    @staticmethod
    def generate(sig_type : Type,amp,freq,shifted):
        # t = np.linspace(0, 2 * np.pi, 1) 
        t = np.arange(0, 2 , 0.01)
        if sig_type == Type.SIN:
            x_t = amp * np.round(np.sin(2*np.pi*freq * t+shifted),3)
        elif sig_type == Type.COS:
             x_t = amp * np.round(np.cos(2*np.pi*freq * t+shifted),3)
        else:
            print("!!TYPE SIGNAL NOT SIN OR COS!!")
            t=0
            x_t = -1
        return t,x_t    