
def word_break(string, words, start=0):
    if start >= len(string):
        return True

    for end in range(start + 1, len(string) + 1):
        print('Checking', string[start:end])
        if string[start:end] in words and word_break(string, words, end):
            return True
    return False

words = set(['a', 'aa'])
print(word_break('aaaaaaaaaa', words))
