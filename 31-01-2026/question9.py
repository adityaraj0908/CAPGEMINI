def longest_common_substring(s1, s2):
    longest = ""

    for i in range(len(s1)):
        for j in range(i + 1, len(s1) + 1):
            sub = s1[i:j]
            if sub in s2:

                if len(sub) > len(longest):
                    longest = sub

    if longest == "":
        return 0
    
    ascii_sum = 0
    for ch in longest:
        ascii_sum = ascii_sum + ord(ch)

    return ascii_sum


s1,s2 = input().split()
print(longest_common_substring(s1,s2))
