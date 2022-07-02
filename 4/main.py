# 2.1. Разработать функцию, возвращающую элементы ряда Фибоначчи по данному максимальному значению.


def fib(n):
    """
    Список чисел ряда Фибоначчи

    Возвращает значения не превосходящие данное n

    Например:
    n = 1, lst = [0, 1, 1]
    n = 2, lst = [0, 1, 1, 2]
    n = 5, [0, 1, 1, 2, 3, 5]

    """
    first = 0
    last = 1

    if n == 0:
        return first
    elif n >= 1:
        for i in range(n - 1):
            _el = first
            first = last
            last = last + _el
        return last
    else:
        raise IndexError


class FibonacchiLst:
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                res = self.instance[self.idx]
            except IndexError:
                raise StopIteration

            self.idx += 1
            return fib(res)


def main():
    # как мы хотим использовать функцию fib, написанную как итератор

    print(list(FibonacchiLst(list(range(10)))))

    # Вариант ответа 1: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    # list(range(10)) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Вариант ответа 2:  [0, 1, 1, 3, 5, 8]


def my_genn():
    l = [1]
    i = 0
    while True:
        yield i + l[-1]
        l.append(i)
        i += 1


g = my_genn()

while True:
    el = next(g)
    print(el)
    if el > 10:
        break


def test_fib_1():
    assert fib(7) == 13, "fib(7), должно быть 13"


def test_fib_2():
    assert fib(4) == 3, "fib(4) должно быть 3"


def feb_iter(iter):
    return list(FibonacchiLst(list(iter)))


from itertools import islice

l = list(range(14))
print('list(range(14))', l, '\nfeb_iter(islice(l,0,4)) = ', feb_iter(islice(l, 0, 4)))

if __name__ == '__main__':
    main()
    test_fib_1()
    test_fib_2()
