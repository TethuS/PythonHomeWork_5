from divisor_master import *

some_number=int(input("Введите число от 1 до 1000:"))

print('Простое число:', Get_prime_number(some_number))

print('Список делителей:', Get_dividers(some_number))

print('Самый большой простой делитель:', Get_max_prime_divider(some_number))