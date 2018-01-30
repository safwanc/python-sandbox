def fibonacci_recursive(n):
    if n in [0, 1]: return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(fibonacci_recursive(10))