""" Solution """
import sys
import math

stdin = int(sys.stdin.readline().strip())

if 1 <= stdin <= 2e9:

    def main(q: int) -> int:
        result = math.ceil(math.log(q,2))
        return result

if __name__ == "__main__":
    print(main(stdin))

##
##
##
""" Tests """
import unittest


class TestCase1(unittest.TestCase):
    def test_1(self):
        result = main(6)
        self.assertEqual(result, 3)

    def test_2(self):
        result = main(5)
        self.assertEqual(result, 3)

    def test_3(self):
        result = main(10)
        self.assertEqual(result, 4)
    
    def test_4(self):
        result = main(9)
        self.assertEqual(result, 4)