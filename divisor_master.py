# Функция проверки, попадает ли введенное число в заданный диапазон
def Get_check(number):
    if number>1000 or number<1: # Проверяем, попадает ли введенное число в заданный диапазон
        return print("ВНИМАНИЕ! Число должно быть в промежутке от 1 до 1000!")
    else:
        return 1

def Get_check_for_one(number):
    if number==1:
        return print('ВНИМАНИЕ! Натуральное число - число больше единицы и имеющее ровно два натуральных делителя!')
    return 1

# Задание 1. Проверка числа на простоту
def Get_prime_number (number):

    if(Get_check(number) and Get_check_for_one(number)):
        divider = 2 # Задаем изначальный делитель
        while number%divider!=0: # Выполняем цикл до тех пор пока не произойдет деление без остатка
            divider+=1 # Наращиваем делитель если деление произошло с остатком
        if divider==number: # Если делитель равен самому числу, то выводим простое число
            return divider


# Задание 2. Выводит список всех делителей числа
def Get_dividers(number):
    if(Get_check(number)):
        divider_list=  [] # Создаем Список делителей
        for i in range(1, number+1): # Циклом проходимся от 1 до Введенного числа
            if number%i==0: # Если происходит деление без остатка, то помещаем число в Список
                divider_list.append(i)
        return divider_list

# Задание 3. Выводит самый большой простой делитель числа.
def Get_max_prime_divider(number):
    if(Get_check(number) and Get_check_for_one(number)):
        all_divider = Get_dividers(number) # Получаем Список делителей числа
        max_divider = 0 # Выделяем переменную под максимальное число
        for i in range(1, len(all_divider)): # Идем циклом со 2го элемента, чтобы не захватывть единицу.
            # Проверяем, является ли число из Списка простым и сравниваем его по величине с Максимальным числом
           if Get_prime_number(all_divider[i]) and Get_prime_number(all_divider[i])>max_divider:
            max_divider=Get_prime_number(all_divider[i]) # Записываем число прошедшее проверку
        return max_divider
