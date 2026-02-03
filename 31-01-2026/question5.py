def product_div_by_7(N):
    product = 1


    my_list = list(map(int,input().split()))


    for i in range(N):
        if my_list[i] % 7 == 0:
            product = product * my_list[i]
            
    return product if product!= 1 else 0
    
    
N = int(input())
print(product_div_by_7(N))
    


