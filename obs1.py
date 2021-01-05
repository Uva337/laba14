#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите следующую задачу: напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е.
# соединение, строк. В остальных случаях введенные числа суммируются.


def get_number01():

    get_number1 = input('Введите 1 число: ')
    get_number2 = input('Введите 2 число: ')
    try:
        if int(get_number1) and int(get_number1):
            c = int(get_number1) + int(get_number2)
            print(c)
    except ValueError:
        print(get_number1 + get_number2)


print(get_number01())
