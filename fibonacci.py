max = 10000000
fibonacci = [1,1]
fibonacci_even = []
summ = 0


while (fibonacci[len(fibonacci)-1]+fibonacci[len(fibonacci)-2]) < max:
    fibonacci.append(fibonacci[len(fibonacci)-1]+fibonacci[len(fibonacci)-2])

print(fibonacci)
print('Количество элементов в последовательности: ' + str(len(fibonacci)))

for i in fibonacci:
    if i % 2 == 0:
        fibonacci_even.append(i)
        summ += i

print('Cумма всех четных элементов: ' + str(summ))

print('Четные элементы: ' + str(fibonacci_even))

print(f'Предпоследнее число последовательности: {fibonacci[len(fibonacci)-2]}')

