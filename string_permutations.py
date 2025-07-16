def fact(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def count_freq(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

def count_permutation(s):
    freq = count_freq(s)
    total = fact(len(s))

    for ch in freq:
        total //= fact(freq[ch])

    return total

s = input()
print(count_permutation(s))
