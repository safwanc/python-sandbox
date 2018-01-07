import collections

def minimum_window_substring(s, t):
    need_characters = collections.Counter(t)
    missing_characters = len(t)

    low_index = substring_start = substring_end = 0
    for high_index, character in enumerate(s, 1):
        if need_characters[character] > 0:
            missing_characters -= 1
        need_characters[character] -= 1

        if not missing_characters:
            while low_index < high_index and need_characters[s[low_index]] < 0:
                need_characters[s[low_index]] += 1
                low_index += 1

            if not substring_end or (high_index - low_index) <= (substring_end - substring_start):
                substring_start, substring_end = low_index, high_index
    
    return s[substring_start:substring_end]

S = 'XADOBECODEBANC'
T = 'ABC'

print(minimum_window_substring(S, T))