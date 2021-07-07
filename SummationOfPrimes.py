primes = []
for num in range(2, 2000000):
    for i in (2, (num)):
        if num % i == 0:
            break
        else:
            primes.append(num)
            total = sum(primes)
            print(total)



