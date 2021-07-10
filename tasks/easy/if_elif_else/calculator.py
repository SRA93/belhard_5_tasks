"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Простой калькулятор

Нужно отредактировать функцию calculator, которая принимает 3 аргумента:
    - Первое число
    - Второе число
    - Операция, которую необходимо выполнить с ними: строка "+", "-", "*", "/"
Функция должна вернуть результат операции или "Неизвестная операция", если
третий аргумент, не указанная операция.

ПРИМЕРЫ
--------------------------------------------------------------------------------
calculator(2, 3, '+') -> 5
calculator(2, 3, '-') -> -1
calculator(2, 3, '*') -> 6
calculator(2, 3, '/') -> 0.6666666666666666
calculator(2, 3, 'no') -> "Неизвестная операция"
"""
from typing import Union


def calculator(num1: int, num2: int, operation: str) -> Union[int, float, str]:

    x = num1
    y = num2
    oper = operation

    if oper in ('+', '-', '*', 'no', '/'):
        if oper == '+':
            print('%.2f + %.2f = %.2f' % (x, y, x + y))
        elif oper == '-':
            print('%.2f - %.2f = %.2f' % (x, y, x - y))
        elif oper == '*':
            print('%.2f * %.2f = %.2f' % (x, y, x * y))
        elif oper == 'no':
            print('Неизвестная операция')
        elif oper == '/':
            if y != 0:
                print('%.2f / %.2f = %.2f' % (x, y, x / y))

    return

if __name__ == '__main__':
    num1_val = int(input('Введите первое число: '))
    num2_val = int(input('Введите второе число: '))
    operation_val = input('Введите операцию: ')
    print(f'Результат: {calculator(num1_val, num2_val, operation_val)}')
