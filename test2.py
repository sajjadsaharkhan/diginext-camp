def remove_chars(s):
    result = []
    for i in range(len(s)):
        if i == 0:
            result.append(s[i])
        elif s[i] != s[i-1]:
            result.append(s[i])
    return "".join(result)

def min_removal(s):
    return len(s) - len(remove_chars(s))

s = "AAABBB"
print(min_removal(s)) # its should return 4