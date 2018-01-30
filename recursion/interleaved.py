def is_interleaved(s1, s2, s3):
    print('Checking s3', s3, 'is interleaved by', s1, 'and', s2)
    if not s1 and not s2 and not s3:
        return True
    elif not s3 and (s2 or s1):
        return False
    
    if s1 and s3[0] == s1[0] and is_interleaved(s1[1:], s2, s3[1:]):
        return True
    elif s2 and s3[0] == s2[0] and is_interleaved(s1, s2[1:], s3[1:]):
        return True
    
    return False


assert(is_interleaved('a', 'b', 'ab') is True)
assert(is_interleaved('a', 'b', 'ba') is True)
assert(is_interleaved('a', 'b', 'aa') is False)
assert(is_interleaved('a', 'b', '') is False)
assert(is_interleaved('a', 'b', 'aba') is False)

assert(is_interleaved('aabcc', 'dbbca', 'aadbbcbcac') is True)
assert(is_interleaved('aabcc', 'dbbca', 'aadbbbaccc') is False)