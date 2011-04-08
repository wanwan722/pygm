import math
import cmath

class DbRefError(Exception):
    pass

def db(amp, ref=1):
    """ Calculate the db value from amplitude, formula: 20 * log(A/Aref) """
    if (ref <= 0):
        raise DbRefError

    if amp > 0:
        return 20 * math.log10(float(amp) / ref)
    else:
        return 0

def idb(db, ref=1):
    """ Calculate the amplitude value from db """
    if (ref <= 0):
        raise DbRefError
    
    return 10 ** (float(db) / 20) * ref

def avg(values):
    sum = 0
    for x in values:
        sum += x
    return sum / len(values)

def aweighting(freq):
    a1 = 12200 ** 2
    a2 = 20.6 ** 2
    a3 = 107.7 ** 2
    a4 = 737.9 ** 2
    a5 = 10 ** (2.0 / 20)
    x = freq ** 2
    return a1 * x * x * a5 / ((x + a2) * (x + a1) * math.sqrt(x + a3) * math.sqrt(x + a4))

def cweighting(freq):
    a1 = 12200 ** 2
    a2 = 20.6 ** 2
    a3 = 10 ** (0.06 / 20)
    x = freq ** 2
    return a1 * x * a3 / ((x + a2) * (x + a1))

def rotate(v, a):
    return v * cmath.rect(1, math.radians(a)) 

def rotate2(x, xa, y, ya):
    return rotate(x, xa) + rotate(y, ya)

class DCOffset:
    def __init__(self):
        self.reset()
    
    def calc(self, values):
        for x in values:
            self.state_ = self.state_ + 1
            coeff = 1.0 / self.state_
            self.value_ = self.value_ * (1 - coeff) + x * coeff
        return self.value
    
    @property
    def value(self):
        return self.value_
    
    def reset(self):
        self.state_ = 0
        self.value_ = 0
        
class RMSDetector:
    def __init__(self):
        self.reset()
    
    def calc(self, values):
        for x in values:
            self.state_ = self.state_ + 1
            coeff = 1.0 / self.state_
            self.value_ = self.value_ * (1 - coeff) + x * x * coeff
        return self.value
    
    @property
    def value(self):
        return math.sqrt(self.value_)
    
    def reset(self):
        self.state_ = 0
        self.value_ = 0

