is_palindrome = lambda string: all(string[i] == string[~i] for i in range(len(string) // 2 + 1))

strings = [
    'aba',
    'aa',
    'b',
    'baa'
]

for string in strings:
    print(string, is_palindrome(string))