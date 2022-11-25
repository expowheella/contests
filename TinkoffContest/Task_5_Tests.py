import unittest
import sys

if __name__ == "__main__":
    stdin = sys.stdin.readline().split()


def main(stdin: list) -> int:
    l = int(stdin[0])
    r = int(stdin[1])
    if ((l >= 1) and (l <= 10**18)) and ((r >= 1) and (r <= 10**18)):
        list = func(l, r)
    else:
        return None
    return len(list)


def func(l, r) -> list:
    list = []
    if l >= 1 and l <= r:

        for i in range(1, 10):
            for j in range(1, 19):
                first_digit = str(i)[0]
                digit = int(first_digit*j)
                if digit >= l and digit <= r and (digit not in list):
                    list.append(digit)

    return list


if __name__ == "__main__":
    print(main(stdin))

# print(main([10,100]))

""" Tests """


class TestCase1(unittest.TestCase):
    def test_1(self):
        result = main([4, 7])
        self.assertEqual(result, 4)

    def test_2(self):
        result = main([10, 100])
        self.assertEqual(result, 9)

    def test_3(self):
        result = main([100, 998])
        self.assertEqual(result, 8)

    def test_4(self):
        result = main([1, 998])
        self.assertEqual(result, 26)


# in order to test in debug mode
if __name__ == '__main__':
    unittest.main()
