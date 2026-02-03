def magic_string_steps(S):
    freq = {}

    for ch in S:
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1

    max_freq = 0
    for value in freq.values():
        if value > max_freq:
            max_freq = value

    steps = len(S) - max_freq
    return steps


s = input()
print(magic_string_steps(s))
