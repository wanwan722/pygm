import unittest
import gmath
import math

class TestMathFunctions(unittest.TestCase):
    def test_db(self):
        self.assertEqual(gmath.db(1), 0)
        self.assertEqual(gmath.db(10), 20)
        self.assertEqual(gmath.db(10, 10), 0)
        self.assertEqual(gmath.db(0.001), -60)
        self.assertAlmostEqual(gmath.db(123, 70), 4.8961414285028220218444698926132)
        self.assertEqual(gmath.db(0), 0)
        
    def test_idb(self):
        self.assertEqual(gmath.idb(-60), 0.001)
        self.assertEqual(gmath.idb(0), 1)
        self.assertEqual(gmath.idb(0, 10), 10)
        self.assertEqual(gmath.idb(95, 11), 618575.45770938398843444614375413)
        
    def test_avg(self):
        self.assertEqual(gmath.avg(range(0, 31)), 15)
    
    def test_aweighting(self):
        self.assertAlmostEqual(gmath.aweighting(0), 0)
        self.assertAlmostEqual(gmath.aweighting(10), 0.00030078281997703)
        self.assertAlmostEqual(gmath.aweighting(30), 0.00932561606168747)
        self.assertAlmostEqual(gmath.aweighting(100), 0.110344916582018)
        self.assertAlmostEqual(gmath.aweighting(1000), 1.00002288818359)
        self.assertAlmostEqual(gmath.aweighting(20000), 0.341170728206635)
        
    def test_cweighting(self):
        self.assertAlmostEqual(gmath.cweighting(0), 0)
        self.assertAlmostEqual(gmath.cweighting(5), 0.0560203120112419)
        self.assertAlmostEqual(gmath.cweighting(15), 0.348896265029907)
        self.assertAlmostEqual(gmath.cweighting(99), 0.965079724788666)
        self.assertAlmostEqual(gmath.cweighting(5000), 0.862109780311584)
        self.assertAlmostEqual(gmath.cweighting(19000), 0.293957978487015)
        
    def test_rotate(self):
        self.assertAlmostEqual(gmath.rotate(3, 0), 3)
        self.assertAlmostEqual(gmath.rotate(5, 90), 5j)
        self.assertAlmostEqual(gmath.rotate(-3, -155), 2.718923361109949889727657970263+1.2678547852220983085609354689432j)
        
    def test_rotate2(self):
        self.assertAlmostEqual(gmath.rotate2(3, 0, 5, 90), 3+5j)
        
    def test_oct1_gain(self):
        #self.assertEqual(gmath.oct1_gain(125, 125), (0.3, -0.3))
        self.assertEqual(gmath.oct1_gain(200, 1000), (-49.6, -gmath.inf))
        self.assertEqual(gmath.oct1_gain(10, 1000), (-70, -gmath.inf))
        self.assertEqual(gmath.oct1_gain(100000, 1000), (-70, -gmath.inf))
        
    def test_oct3_gain(self):
        self.assertEqual(gmath.oct3_gain(125, 125), (0.3, -0.3))
        self.assertEqual(gmath.oct3_gain(200, 1000), (-68.984341938214129, -gmath.inf))
        self.assertEqual(gmath.oct3_gain(10, 1000), (-70, -gmath.inf))
        self.assertEqual(gmath.oct3_gain(100000, 1000), (-70, -gmath.inf))
        
    def test_dcoffset(self):
        values = range(1, 11)
        dc = gmath.DCOffset()
        self.assertEqual(dc.calc(values), 5.5)
        self.assertEqual(dc.value, 5.5)
        
    def test_rmsdetector(self):
        values = range(1, 3)
        ideal = 0.0
        for x in values:
            ideal += x * x
        ideal = math.sqrt(ideal / len(values))
        rms = gmath.RMSDetector()
        self.assertEqual(rms.calc(values), ideal)
        self.assertEqual(rms.value, ideal)

if __name__ == '__main__':  
    unittest.main()