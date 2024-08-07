import numpy as np 
#Advanced Array Operations:
#Create a 2-D array with 1 on the border and 0 inside. 
'''r=4
arr1=np.zeros((4,4))
for i in range(r):
    for j in range(r):
        if i == 0 or i == r-1 or j == 0 or j == r-1:
            arr1[i][j] = 1

print(f'modified array =\n{arr1}')
'''
#Multiply a 5x3 matrix by a 3x2 matrix using matrix multiplication. 
#r1=int(input('enter number of Rows'))
#c1=int(input('enter number of Columns'))
mat1 = np.random.rand(5, 3)
print(f'Array 1=\n{mat1}')
mat2 = np.random.rand(3, 2)
print(f'Array 2=\n{mat2}')
#arr2 = [[int(input(f"Enter element at position ({i+1}, {j+1}): ")) for j in range(c1)] for i in range(r1)]
result=np.dot(mat1,mat2)
print(f'Multiplied Array=\n{result}')
#Compute the inverse and determinant of a square matrix.
