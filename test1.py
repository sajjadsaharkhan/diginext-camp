def repeat_string(s, n):
    result = s * (n // len(s)) + s[:n % len(s)]
    count_a = result.count("a")
    print(result)
    return count_a

s = "aba"
n = 10
print(repeat_string(s, n)) # it should print 4
