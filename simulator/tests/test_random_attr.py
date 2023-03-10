from simulator.animal import random_attr
import unittest
import yaml

print(random_attr.RandomAttr.age())


class TestRandomAttr(unittest.TestCase):
    stream = open("../config.yaml", "r")
    data = yaml.safe_load(stream)

    def test_age(self):
        self.assertIs(type(random_attr.RandomAttr.age()), int)
        self.assertLessEqual(random_attr.RandomAttr.age(), self.data["age"][1])
        self.assertGreaterEqual(random_attr.RandomAttr.age(), self.data["age"][0])


#
if __name__ == '__main__':
    unittest.main()
