fact_factors = []
a = 0
i = ()
for i in range (1, 101):
    z = (a + i)
    fact_factors.append(z)
product = 1
for item in fact_factors:
    product = product * item
digits = [int(x) for x in str(product)]
c = sum(digits)
print(c)