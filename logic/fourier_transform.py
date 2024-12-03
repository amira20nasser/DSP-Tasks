import numpy as np
import math
import cmath
class FourierTransform:
    
    @staticmethod
    def dtf_transform(signal ,fs):
        x_k_amplitude = []
        x_k_phase =[]
        length = len(signal)
        for k in range(fs): 
            res = 0
            for n in range(length):
                pow=-1j*k*math.pi*n/length
                res+=signal[n]*cmath.exp(pow)
            amplitude=cmath.polar(res)[0]
            phase=cmath.polar(res)[1]
            x_k_amplitude.append(amplitude)
            x_k_phase.append(phase)
        print("amplitude", x_k_amplitude)
        print("phase", x_k_phase)

        return x_k_amplitude, x_k_phase       # return amplitude and phaseshift 
       
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
            x_n.append(round(sumk.real/length))

        return x_n
            

#Use to test the Amplitude of DFT and IDFT
    @staticmethod
    def SignalComapreAmplitude(SignalInput = [] ,SignalOutput= []):
        if len(SignalInput) != len(SignalOutput):
            return False
        else:
            for i in range(len(SignalInput)):
                if abs(SignalInput[i]-SignalOutput[i])>0.001:
                    return False
                elif SignalInput[i]!=SignalOutput[i]:
                    return False
            return True
    @staticmethod
    def RoundPhaseShift(P):
        while P<0:
            p+=2*math.pi
        return float(P%(2*math.pi))

    #Use to test the PhaseShift of DFT
    @staticmethod
    def SignalComaprePhaseShift(SignalInput = [] ,SignalOutput= []):
        if len(SignalInput) != len(SignalOutput):
            return False
        else:
            for i in range(len(SignalInput)):
                A=round(SignalInput[i])
                B=round(SignalOutput[i])
                if abs(A-B)>0.0001:
                    return False
                elif A!=B:
                    return False
            return True

