from simulator.Animal.random_characteristics import RandomAttr
import yaml
import unittest

stream = open("../../config.yaml", "r")
data = yaml.safe_load(stream)

print(RandomAttr.age())


class TestRandomAttr(unittest.TestCase):

    def test_age(self):
        self.assertIs(type(RandomAttr.age()), int)
        self.assertLessEqual(RandomAttr.age(), data["age"][1])
        self.assertGreaterEqual(RandomAttr.age(), data["age"][0])




#
if __name__ == '__main__':
    unittest.main()
