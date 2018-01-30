n = 8


for i in range(1, int(pow(n, 0.5) + 1)):
    if (n % i) == 0:
        print(i)