
                 # smart soluttion
#def is_prime(n):
#    if n == 1:
#        return False
#    i = 2)
#    while i*i <= n:
#        if n % i == 0:
#            return False
#        i += 1
#    return True
#sumPrime = 0
#for num in range(1, 2000000):
#    if is_prime(num):
#        print(num)
#        sumPrime += num
#print('sumPrime', sumPrime)





                # OG solution
primes = []
for num in range(2, 2000000):
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            primes.append(num)
            total = sum(primes)
            print(total)
