import math
import cmath
import numpy
import scipy.interpolate

inf = float('inf')

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

def _get_0darray(arr):
    return arr.flat.next()

def _oct_gain(f, b, x):
    y1 = numpy.array([-70, -61, -42, -17.5, -2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
                      0.3, 0.3, 0.3, -2.0, -17.5, -42, -61, -70])
    y2 = numpy.array([-inf, -inf, -inf, -inf, -5, -5, -1.3, -0.6, -0.4, -0.3,
                      -0.4, -0.6, -1.3, -5, -5, -inf, -inf, -inf, -inf])
    
    c1 = scipy.interpolate.interpolate.interp1d(x, y1, bounds_error=False, fill_value=-70)
    c2 = scipy.interpolate.interpolate.interp1d(x, y2, bounds_error=False, fill_value=-inf)
    r1 = _get_0darray(c1(f))
    r2 = _get_0darray(c2(f))
    if numpy.isnan(r2):
        r2 = -numpy.inf
    return (r1, r2)

def oct1_gain(f, b):
    x = numpy.array([2**-4, 2**-3, 2**-2, 2**-1, 2**-(1.0/2), 2**-(1.0/2),
                     2**-(3.0/8), 2**-(1.0/4), 2**-(1.0/8), 1, 2**(1.0/8),
                     2**(1.0/4), 2**(3.0/8), 2**(1.0/2), 2**(1.0/2), 2**1,
                     2**2, 2**3, 2**4])
    return _oct_gain(f, b, b * x)
    
def oct3_gain(f, b):
    x = numpy.array([0.184, 0.32578, 0.52996, 0.77181, 0.8909, 0.8909, 0.91932,
                     0.94702, 0.97394, 1, 1.02676, 1.05594, 1.08776, 1.12246,
                     1.12246, 1.29565, 1.88695, 3.06955, 5.43474])
    return _oct_gain(f, b, b * x)

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

