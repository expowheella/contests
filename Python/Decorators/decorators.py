""" Simple Decorator 1"""

# def my_decorator1(func):
#     def wrapper():
#         print('------')
#         func()
#         print('------')
#     return wrapper

# @my_decorator1
# def hello():
#     print("Hellllooooo")

# hello()


""" Simple Decorator 2 """

def my_decorator2(func):
    def wrapper():
        print('-2-2-2-2-2-2-')
        func()
        print('-2-2-2-2-2-2-')
    return wrapper

def bye():
    print("Byyyyyyeeeee")

# decorate = my_decorator2(bye)
# decorate()

my_decorator2(bye)()
