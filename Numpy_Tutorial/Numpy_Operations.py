import numpy as np 
'''
def myadd(x, y,z):
  return x+y+z

myadd = np.frompyfunc(myadd, 3, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8],[1,4,3,2]))
print(type(np.add))'''

#Arithmatic
arr1 = np.array([10, 20, 30])
arr2 = np.array([3, 5, 10])

newarr2 = np.add(arr1, arr2)
newarr1 = np.subtract(arr1, arr2)
newarr3 = np.divide(arr1, arr2)
newarr4 = np.multiply(arr1, arr2)
newarr5 = np.mod(arr1, arr2)
newarr6 = np.divmod(arr1, arr2)
newarr7 = np.power(arr1, arr2)
#statical function
newarr8 = np.mean(arr1)
newarr9 = np.median(arr1)
newarr10 = np.std(arr1)
newarr11= np.var(arr1)

print(newarr2)
print(newarr1)
print(newarr3)
print(newarr4)
print(newarr5)
print(newarr6)
print(newarr7)
print(newarr8)
print(newarr9)
print(newarr10)
print(newarr11)