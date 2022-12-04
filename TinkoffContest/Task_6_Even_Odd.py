import sys
from typing import List, TypeVar
import unittest

T = TypeVar('T', int, int)

if __name__ == "__main__":
    stdin1 = sys.stdin.readline().split()
    stdin1 = [int(i) for i in stdin1 if int(i) >= 2 and int(i) <= 1000]

    stdin2 = sys.stdin.readline().split()
    stdin2 = [int(i) for i in stdin2 if int(i) >= 1 and int(i) <= 10**9]


def main(stdin1, stdin2) -> List[T]:
    if stdin1[0] == len(stdin2):
        even, odd = list(), list()
        for num, i in enumerate(stdin2, 1):
            if (num % 2 == 1) and (i % 2 == 0):
                even.append(num) # четная цифра на нечетной позиции, поэтому добавим номер позиции в список
            elif (num % 2 == 0) and (i % 2 == 1):
                odd.append(num) # нечетная цифра на четной позиции, поэтому добавим номер позиции в список
            else:
                continue

        if len(even) == len(odd) and len(odd) == 1:
            print(even[0], odd[0])
            return even[0], odd[0]
        # elif len(stack) % 2 == 0 and len(stack) > 2:
        #     print(stack[0], stack[1])
        #     return stack[0], stack[1]
        else:
            stack = [-1, -1]
            print(stack[0], stack[1])
            return stack[0], stack[1]
    else:
        stack = [-1, -1]
        print(stack[0], stack[1])
        return stack[0], stack[1]


if __name__ == "__main__":
    main(stdin1, stdin2)


""" Tests """


class TestCase1(unittest.TestCase):
    def test_1(self):
        result = main([2], [2, 1])
        self.assertEqual(result, (1, 2))

    def test_2(self):
        result = main([4], [2, 1, 4, 6])
        self.assertEqual(result, (-1, -1))

    def test_3(self):
        result = main([2], [1, 2])
        self.assertEqual(result, (-1, -1))

    def test_4(self):
        result = main([6], [1, 2, 4, 3, 5, 6])
        self.assertEqual(result, (3, 4))

    def test_5(self):
        result = main([8], [1, 2, 4, 3, 5, 6, 8, 7])
        self.assertEqual(result, (-1, -1))

    def test_6(self):
        result = main([8], [4, 3, 2, 1, 6, 11, 8, 7])
        self.assertEqual(result, (-1, -1))


# in order to test in debug mode
if __name__ == '__main__':
    unittest.main()
