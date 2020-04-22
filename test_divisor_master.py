from divisor_master import *

# Проверка на простое число
def test_divisor_master_prime_1():
    assert Get_prime_number(1)== None # Проверка вывода при вводе единицы, которая является спорным простым числом

def test_divisor_master_NOprime():
    assert Get_prime_number(879) == None  # Проверка вывода НЕ простого числа

def test_divisor_master_prime():
    assert Get_prime_number(577) == 577  # Проверка вывода простого числа

# Проверка на список делителей
def test_divisor_master_deviders_1():
    assert Get_dividers(1)== [1] # Проверка списка делителей при вводе единицы

def test_divisor_master_deviders_NOprime():
    assert Get_dividers(12)==[1, 2, 3, 4, 6, 12] # Проверка списка делителей при вводе НЕ простого числа

def test_divisor_master_deviders_prime():
    assert Get_dividers(199) == [1, 199] # Проверка списка делителей при вводе простого числа

# Провекра на самый большой простой делитель
def test_divisor_master_max_prime_divider_1():
    assert Get_max_prime_divider(1)== None # Проверка на самый большой простой делитель при вводе единицы

def test_divisor_master_max_prime_divider_NOprime():
    assert Get_max_prime_divider(720) == 5 # Проверка на самый большой простой делитель при вводе НЕ простого числа

def test_divisor_master_max_prime_divider_prime():
    assert Get_max_prime_divider(137) == 137 # Проверка на самый большой простой делитель при вводе НЕ простого числа


