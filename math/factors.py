n = 864


for i in range(1, int(pow(n, 0.5) + 1)):
    if (n % i) == 0:
        print(i)

def prime_factors(n):
    d = 2
    factors = [ ]  #empty list
    while n > 1:
      if n % d == 0:
        factors.append(d)
        n = n/d
      else:
        d = d + 1
    return factors

print(prime_factors(n))