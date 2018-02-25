fib_recursive = lambda n: fib_recursive(n-1) + fib_recursive(n-2) if n > 1 else n

fibs = {0: 0, 1: 1}
def fib(n):
    if n not in fibs:
        fibs[n] = fib(n-1) + fib(n-2)
    return fibs[n]

assert(fib(300) == 222232244629420445529739893461909967206666939096499764990979600)