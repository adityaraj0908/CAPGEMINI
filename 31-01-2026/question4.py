def no_of_vacant_rooms(N, A, T):

    vacant = T - N
    return vacant


N = int(input())
rooms = list(map(int,input().split()))
total_rooms = int(input())

print(no_of_vacant_rooms(N,rooms,total_rooms))
