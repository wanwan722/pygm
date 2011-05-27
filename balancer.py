import math
import cmath

class mass:
    weight = 0
    angle = 0
    def __init__(self, weight = 0, angle = 0):
        self.weight = weight
        self.angle = angle
    
    @property    
    def cplx(self):
        return cmath.rect(self.weight, math.radians(self.angle))

class vib:
    magn = 0
    phase = 0
    def __init__(self, magn = 0, phase = 0):
        self.magn = magn
        self.phase = phase

    @property
    def cplx(self):
        return cmath.rect(self.magn, math.radians(self.phase))

class rotor:
    ubalance = 0.0
    trail = 0.0
    step = 0
    balance_mass = []
    def __init__(self, unbalance):
        self.ubalance = unbalance
        pass
    
    def trial(self, mass, method='add', after='remove'):
        self.trail = mass

    def add_mass(self, mass):
        self.balance_mass.add(mass)

    def calc(self):
        result = 0.0
        return result
    
class coeff:
    v0 = vib()
    vt = vib()
    mt = mass()
    def __init__(self):
        pass
    
    def calc(self):
        assert(self.mt != 0)
        return (self.vt.cplx - self.v0.cplx) / self.mt.cplx

class balance_method:
    coeff = coeff()
    k = 0
    def __init__(self):
        pass

    def set_v0(self, vib):
        self.coeff.v0 = vib
        
    def calc(self, vib):
        return coeff.calc() / vib

    
