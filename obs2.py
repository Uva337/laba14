from random import randint

try:
    import random

    N = int(input('строки -> '))
    M = int(input('столбцы -> '))
    c = int(input('начало диапазона целых чисел -> '))
    d = int(input('конец диапазона целых чисел -> '))
    lst = [[randint(c, d) for i in range(N)] for i in range(M)]
    for i in lst:
        print()
        for j in i:
            print(j, end=" ")
except ValueError:
    print("Ошибка, повторите снова!")
else:
    print("\nВыполняется, если не было ошибок!")
finally:
    print("Выполняется всегда!")