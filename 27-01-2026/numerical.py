import numpy as np

# a1 = np.array([1,2,3])
# a2 = np.array([[1,2],[3,4]])
# a3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])


# a0 = np.zeros((3,3))
# a1 = np.ones((2,2))
# a2 = np.arange()

# print(a0)
# print(a1)
# print(a2)






# a1 = np.array([10,20,30,40,50])
# print(a1[2])
# print(a1[-1])


# a2 = np.array([
#             [1,2,3],
#               [4,5,6],
#               [7,8,9]])
# print(a2[1,0])




# a = np.array([10,20,30,40,50,60])
# idx = np.array([1,3,5])


# print(a[idx])

# cond = a>30
# print(a[cond])




# x = np.array([1,2,3])
# y = np.array([4,5,6])

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)



# a1 = np.array([1,2,3])
# a2 = np.array([4,5,6])

# res = np.add(a1,a2)
# print(res)








# a = np.array([0,np.pi/2,np.pi])
# print(np.sin(a))

# b = np.array([0,1,2,3])
# print(np.exp(b))
# print(np.sqrt(b))

# print(np.sqrt(a))











# dtype = [('name','S10'),('year',int),('cgpa',float)]

# vals = [("hritik",2009,8.9),
#         ("Ramhul",2020,9.1),
#         ("Pankaj",2021,7.0)]


# a = np.array(vals,dtype=dtype)

# print(np.sort(a,order='name'))
# print(np.sort(a,order=['year','cgpa']))









# print(np.zeros((2,3)))
# print(np.ones((3,2)))
# print(np.full((2,2),7))
# print(np.arange(0,10,2))
# print(np.linspace(0,10,4))










# print(np.random.rand(2,3))
# print(np.random.rand(2,2))
# print(np.random.randint(1,10,size=(2,3)))







# k = np.eye(3)
# print(k)
# print(np.diag([1,2,3]))
# print(np.zeros_like(k))
# print(np.ones_like(k))

# print(np.random.randint(0,10, size =(2,3)))
# print(np.random.randint(5,15,size=(2,2,4)))




# import numpy as np
# x = np.random.normal()
# print(x)






import matplotlib.pyplot as plt
from scipy.stats import binom
n = 10
p = 0.5
size = 1000
data = np.random.binomial(n,p,size)
plt.hist(data, bins = np.arange(-0.5, n+1.5, 1), density=True, edgecolor='black', alpha=0.7, label='Histogram')
x = np.arange(0, n+1)
pmf = binom.pmf(x,n,p)
plt.scatter(x, pmf, color='red', label='Theroretical PMF')
plt.vlines(x, 0, pmf,colors='red', linestyles='dashed')
plt.title("Binomial distribution (n=10, p=0.5)")
plt.xlabel("Number of successes")
plt.ylabel("Probability")
plt.legend()
plt.grid(True)
plt.show()
