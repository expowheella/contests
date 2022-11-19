import sys
import unittest


def parse(stdin):
    list = [int(i) for i in stdin if int(i) <= 1000000]
    return list


collection = []


def main(stdin1, stdin2):
    count = stdin1[1]
    numbers = stdin2
    numbers.sort(reverse=True)
    

    mtrx = matrix(numbers)
    print(mtrx)

    diff = []
    for i in mtrx:
        digit = min(i)
        pow = 10**(len(str(digit))-1)
        head = (digit// pow) * pow
        tail = digit % pow
        diff.append((9*pow) - head)
        print(" ")

    

def matrix(numbers):
    limit = len(str(numbers[0]))
    result_list = []
    while limit != 0:
        if len(result_list)>0:
            result_list.pop(-1)
        new_list, numbers = detacher(numbers)
        result_list.append(new_list)
        if len(numbers)>0:
            result_list.append(numbers)
        limit -= 1

    
    return result_list


def detacher(numbers):
    new_list, second_list = [], []
    length = len(str(numbers[0]))
    for i in numbers:
        if len(str(i)) == length:
            new_list.append(i)
        else:
            second_list.append(i)
    return new_list, second_list

    maximum = len(str(max(numbers)))

    pow = 10**(maximum-1)

    head_list, tail_list = [], []
    for i in numbers:
        while count != 0:
            head = (i // pow) * pow
            tail = i % pow

            head_list.append(head)
            tail_list.append(tail)

            diff = (9*pow) - min(head_list)
            collection.append(diff)
            count -= 1

    stdin2 = tail_list

    result = sum(collection)
    print(result)
    return result


if __name__ == "__main__":
    stdin1 = sys.stdin.readline().split()  # n-digits, k-chances
    stdin2 = sys.stdin.readline().split()  # list of numbers

    stdin1 = parse(stdin1)
    stdin2 = parse(stdin2)

    stdin2 = main(stdin1, stdin2)


class TestCase1(unittest.TestCase):
    def test_1(self):
        result = main([5, 2], [1, 2, 1, 3, 5])
        self.assertEqual(result, 16)

    def test_2(self):
        result = main([3, 1], [99, 5, 85])
        self.assertEqual(result, 10)
