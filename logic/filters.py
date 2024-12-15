from enum import Enum

class Type(Enum):
    LOW_PASS = 'Low Pass'
    HIGH_PASS = 'High Pass'
    BAND_PASS = 'Band Pass'
    BAND_REJECT = 'Band Reject'
