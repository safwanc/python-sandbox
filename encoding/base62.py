from collections import deque
import string

initial = 1231231232919091181881  # base 10
encoded = deque()

while initial:
    initial, remainder = divmod(initial, 62)
    encoded.appendleft(remainder)

letters = list(string.ascii_letters + string.digits)
print(encoded, '➡', ''.join(letters[i] for i in encoded))