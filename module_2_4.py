numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 163, 289, 3571, 15874, 26565, 615053, 12752041]
primes = []
not_primes = []
for i in range (len(numbers)):
    for j in range (2, max(numbers)):
        if numbers[i] < j:
            break
        if numbers[i] % j == 0:
            if numbers[i] != j and numbers[i] != 1:
                not_primes.append(numbers[i])
            else:
                primes.append(numbers[i])
            break
print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')
