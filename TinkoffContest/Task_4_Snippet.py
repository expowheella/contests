import sys
import unittest


def parse(stdin):
    list = [int(i) for i in stdin if int(i) <= 10**4 and int(i) >= 1]
    return list


def main(stdin1, stdin2):
    if stdin1[0] <= 0:
        return None
    elif len(stdin2)!= stdin1[0]:
        return None
    count = stdin1[1]
    numbers = stdin2
    numbers.sort()

    result = []
    while count != 0:
        diff, count = run(numbers, count)
        result.append(sum(diff))
        if len(result) > stdin1[1]:
            break

    print(sum(result))
    return sum(result)


def run(numbers, count):
    diff = []

    for index, i in enumerate(numbers):

        if len(str(max(numbers))) == len(str(i)) and i >= 1:
            pow = 10**(len(str(i))-1)
            head = (i // pow) * pow
            tail = i % pow
            diff.append((9*pow) - head)
            numbers.pop(index)
            numbers.append(tail)
            numbers.sort()
            count -= 1
            if count == 0 or diff[0] == 0:
                break
    return diff, count


if __name__ == "__main__":
    stdin1 = sys.stdin.readline().split()  # n-digits, k-chances
    stdin2 = sys.stdin.readline().split()  # list of numbers

    stdin1 = parse(stdin1)
    stdin2 = parse(stdin2)

    sum_diff = main(stdin1, stdin2)


class TestCase1(unittest.TestCase):
    def test_1(self):
        result = main([5, 2], [1, 2, 1, 3, 5])
        self.assertEqual(result, 16)

    def test_2(self):
        result = main([3, 1], [99, 5, 85])
        self.assertEqual(result, 10)

    def test_3(self):
        result = main([1, 10], [9999])
        self.assertEqual(result, 0)

    def test_4(self):
        result = main([1, 10], [9998])
        self.assertEqual(result, 1)

    def test_5(self):
        result = main([3, 10], [99, 5, 85])
        self.assertEqual(result, 18)

    def test_6(self):
        result = main([0, 10], [99, 5, 85])
        self.assertEqual(result, None)

    def test_7(self):
        result = main([1, 10], [9999, 9998])
        self.assertEqual(result, None)

    def test_8(self):
        result = main([2, 10], [1, 9998])
        self.assertEqual(result, 9)