import sys
sys.path.append('../lib')

from random_characteristics import *
import unittest


class TestRandomAttr(unittest.TestCase):

    def test_age(self):
        self.assertTrue(age() is int)
        self.assertTrue(x <= age() <= y)
        assert 1 <= RandomAttr.age() <= 6

    # def test_weight_type(self):
    #     assert type(RandomCharacteristics.weight()) is int
    #     assert 1 <= RandomCharacteristics.weight() <= 400

# class TestRandomAttr(unittest.TestCase):
#     def test_age(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()
