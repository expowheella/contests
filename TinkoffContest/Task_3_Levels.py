""" 
n - договоров 
m - этажей

проход по этажам занимает 1 минуту:
(m+1)/1 или 
(m-1)/1

один из коллег уйдет через t минут 

"""

""" Solution """
import sys
import unittest


def parse(stdin):
    list = [int(i) for i in stdin if int(i) <= 100]
    return list


if __name__ == "__main__":
    stdin1 = sys.stdin.readline().split() # кол-во сотрудников, время, когда уйдет первый сотрудник
    stdin2 = sys.stdin.readline().split() # номера этажей
    stdin3 = sys.stdin.readline().split() # номер сотрудника, который уйдет первым

    stdin1 = parse(stdin1)
    stdin2 = parse(stdin2)
    stdin3 = parse(stdin3)


def main(stdin1, stdin2, stdin3):
    n_t = parse(stdin1)
    n = n_t[0]
    t = n_t[1]
    firstOut = parse(stdin3)[0] - 1

    levels = parse(stdin2)

    level = levels[firstOut]  # этаж, с которого уходит первый сотрудник
    max = levels[-1]  # верхний этаж
    min = levels[0]  # нижний этаж

    if 2 <= n <= 100 and 2 <= t <= 100:

        if (level - min) > t and (max - level) > t:  # значит нужно начать с этого сотрудника
            case1 = max - min + max - level
            case2 = max - min + level - min
            if case1 > case2:
                print(case2)
                return case2
            else:
                print(case1)
                return case1
        elif level - min <= t:  # begin from minimum level
            result = max - min
            print (result)
            return result
        elif max - level <= t:
            result = max - min
            print (result)
            return result

        elif level == max:
            result = max - min
            print (result)
            return result

        elif level == min:
            result = level - min + max - min
            print(result)
            return result

    else:
        return None


if __name__ == "__main__":
    main(stdin1, stdin2, stdin3)



class TestCase1(unittest.TestCase):
    def test_1(self):
        count = main([5, 5], [1, 4, 9, 16, 25], [2])
        self.assertEqual(count, 24)

    def test_2(self):
        count = main([6, 4], [1, 2, 3, 6, 8, 25], [5])
        self.assertEqual(count, 31)

    def test_3(self):
        count = main([2, 2], [1, 2, 3, 6, 8, 25], [5])
        self.assertEqual(count, 31)

    def test_4(self):
        count = main([25, 25], [1, 2, 3, 6, 8, 25], [5])
        self.assertEqual(count, 24)

    def test_5(self):
        count = main([25, 2], [1, 5, 25], [2])
        self.assertEqual(count, 28)

    def test_6(self):
        count = main([25, 2], [1, 5, 25], [3])
        self.assertEqual(count, 24)

    def test_7(self):
        count = main([2, 100], [4, 5, 100], [2])
        self.assertEqual(count, 96)

    def test_8(self):
        count = main(
            [2, 3],            # кол-во сотрудников; время, когда уйдет первый сотрудник          
            [2, 3, 4, 5, 7, 10, 20, 100], # номера этажей
            [3]                # номер сотрудника, который уйдет первым
        )
        self.assertEqual(count, 98)

    def test_9(self):
        count = main(
            [2, 2],            # кол-во сотрудников; время, когда уйдет первый сотрудник          
            [1, 20], # номера этажей
            [1]                # номер сотрудника, который уйдет первым
        )
        self.assertEqual(count, 19)

    def test_10(self):
        count = main(
            [2, 2],            # кол-во сотрудников; время, когда уйдет первый сотрудник          
            [1, 20], # номера этажей
            [2]                # номер сотрудника, который уйдет первым
        )
        self.assertEqual(count, 19)


    def test_11(self):
        count = main(
            [4, 4],            # кол-во сотрудников; время, когда уйдет первый сотрудник          
            [2, 5, 7, 11], # номера этажей
            [3]                # номер сотрудника, который уйдет первым
        )
        self.assertEqual(count, 9)