import doctest
import unittest
import yurlungur as yr

class TestApp(unittest.TestCase):
    def test_maya(self):
        yr.application.mayapy("import sys; print sys.path")

if __name__ == '__main__':
    unittest.main()