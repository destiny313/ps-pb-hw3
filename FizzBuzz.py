# Еще одна популярная задача - FizzBuzz: если число делится на 3, то нужно вывести Fizz, если на 5, то Buzz, если на 3 и на 5, то FizzBuzz.
#
# Задача - написать программу, которая выводит сумму чисел из диапазона от 1000 до 20000 включительно, которые делятся и на 3 и на 5.

def fizzbuz (number):
    '''
    Функция принимает число и возвращает True, в случае если оно делится и на 3 и на 5
    :param number: - число
    '''
    result = False
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
        result = True
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')

    return result


summ = 0

for i in range(1000,20001):
    if fizzbuz(i):
        summ += i

print('Сумма: ' + str(summ))