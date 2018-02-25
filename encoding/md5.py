import hashlib
import string
import collections

base10to62 = {i: c for i, c in zip(range(62), string.ascii_letters + string.digits)}
base62to10 = {c: i for i, c in base10to62.items()}

'''
MD5
'''
hasher = hashlib.md5()
hasher.update(b"http://thisisavery.com/longurl/that/youshould/shorten.html")


'''
Encode
'''
base16 = hasher.hexdigest()
base10 = int(base16, base=16)
print('Base 16: ', base16)
print('Base 10: ', base10)

base62 = collections.deque()

while base10:
    base10, remainder = divmod(base10, 62)
    base62.appendleft(base10to62[remainder])

base62 = ''.join(base62)
print('Base 62: ', base62)

print('-' * 100)

'''
Decode
'''
encoded = list(base62)[::-1]

# multiplier, base10 = 1, 0
# while encoded:
#     base10 += multiplier * base62to10[encoded.pop()]
#     multiplier *= 16
#     print(base10, multiplier)
    
# print(base10)