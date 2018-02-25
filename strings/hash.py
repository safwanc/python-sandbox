import hashlib

string = b'This is a test string'
print(string)
hashed = hashlib.md5(string)
print(hashed.hexdigest())