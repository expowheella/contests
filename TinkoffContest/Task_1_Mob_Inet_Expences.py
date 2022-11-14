""" Solution """
import sys

stdin = sys.stdin.readline().split()
stdin = [int(i) for i in stdin]

keys = ["A", "B", "C", "D"]
stdin = dict(zip(keys, stdin))


def main(a: int, b: int, c: int, d: int) -> int:
    if d > b:
        result = (d - b) * c + a
        return result
    else:
        return a


if __name__ == "__main__":
    print(main(stdin["A"], stdin["B"], stdin["C"], stdin["D"]))

##
##
##
""" Tests """
import unittest


class TestCase1(unittest.TestCase):
    def test_1(self):
        result = main(100, 10, 12, 15)
        self.assertEqual(result, 160)

    def test_2(self):
        result = main(100, 10, 12, 1)
        self.assertEqual(result, 100)
