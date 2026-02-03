import math

def no_of_rounds(C,N):
    return math.ceil(N/C)

C,N = map(int,input().split())

print(no_of_rounds(C,N))