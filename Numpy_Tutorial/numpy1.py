import numpy as np

'''arr = np.array(["n", 2, 3, 4, 5])
arr2 = np.array([[[1, 2,4] ,[4, 5,4]],[[1, 2,4] ,[4, 5,4]]])
print(arr)
print(arr2)
print(arr.ndim)
print(arr2.ndim)
print(arr.shape)
print(arr2.shape)
print(arr.dtype)'''

'''a=np.zeros((2, 2))
print(f'array with 2*2 having all zeros \n{a}')
b=np.ones((3, 3))
print(f'array with 3*3 having all Ones\n{b}')
c=np.full((2, 2), 7)
print(f'array with full having all seven\n{c}')
d=np.eye(3)
print(f'array with diagonal elemet as 1 \n{d}')
e=np.random.random((2, 2))
print(f'array with random values\n{e}')'''

'''#Reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr2d = arr.reshape(4, 3)
newarr3d = arr.reshape(2, 3,2)
print(newarr2d)
print(newarr3d)
# Multidinestion to 1D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)'''

#iteration
#1D
arr = np.array([1, 2, 3])
for x in arr:
  print(x)
#2D
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr2:
  print(x)

#Ieration through each element
arr3 = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr3:
  for y in x:
    print(y)
#3d

arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr4:
  for y in x:
    for z in y:
      print(z)

#Itearate with positions
      
arr5 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr5):
  
  if arr5[idx][x] == 6:
    print(idx, x)

#Joining of array
arr6 = np.array([1, 2, 3])

arr7 = np.array([4, 5, 6])

arrfinal = np.concatenate((arr6, arr7))

print(arr)