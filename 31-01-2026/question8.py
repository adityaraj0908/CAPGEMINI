H, V, Vn = map(int,input().split())

e = V / Vn

rebound_height = H * (e * e)

print(int(rebound_height))
