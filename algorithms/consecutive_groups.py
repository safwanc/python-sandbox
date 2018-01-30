def get_consecutive_groups(iterable):
    s = tuple(iterable)
    for size in range(1, len(s) + 1):
        for index in range(len(s) + 1 - size):
            yield iterable[index:index+size]

print(list(get_consecutive_groups('abcde')))
print(list(get_consecutive_groups([1, 2, 3, 4])))