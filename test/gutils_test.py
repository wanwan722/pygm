import unittest
import gutils

class TestUtilsFunctions(unittest.TestCase):
    def test_error_rate(self):
        self.assertEqual(gutils.error_rate(1, 1), 0)
        self.assertEqual(gutils.error_rate(1, 2), -50)
        self.assertEqual(gutils.error_rate(10, 2), 400)
        self.assertEqual(gutils.error_rate(0, 0), 0)

if __name__ == '__main__':  
    unittest.main()