n = int(input('Введите число: '))
key = []
a = int(n / 2)
for i in range(1, a + 1):
    for j in range(1, n):
        b = i + j
        if n % b == 0 and i < j:
            key.append(i)
            key.append(j)
str_numbers = [str(k) for k in key]  # гугление
result = ' '.join(str_numbers)  # гугление
print(f'для числа {n} ключ: {result}')



