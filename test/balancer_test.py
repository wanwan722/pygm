import unittest

import sys
sys.path.append('../')

import balancer
import cmath

class TestMass(unittest.TestCase):
    def test_init(self):
        m = balancer.mass(5, 30)
        self.assertEqual(m.weight, 5)
        self.assertEqual(m.angle, 30)
        m = balancer.mass()
        self.assertEqual(m.weight, 0)
        self.assertEqual(m.angle, 0)

class TestHelperFunction(unittest.TestCase):
    def test_mass(self):
        pass
        #self.assertEqual(balancer.mass(3, 0), cmath.rect(3, 0))
        #self.assertEqual(balancer.mass(5, 90), cmath.rect(5, cmath.pi / 2))

class TestBalancer(unittest.TestCase):
    def test_basic(self):
        unbalance = balancer.mass(4, 90)
        rotor = balancer.rotor(unbalance)
        rotor.calc()
        
class TestCoeff(unittest.TestCase):
    def test_calc(self):
        coeff = balancer.coeff()
        coeff.v0 = balancer.vib(2, 2)
        coeff.mt = balancer.mass(5, 1)
        k = coeff.calc()

if __name__ == '__main__':  
    unittest.main()