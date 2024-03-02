import numpy as np
import numpy.linalg as lg

mx_1=[]
mx_2=[]

matrix_1=[[1,2],
          [3,4]]
matrix_2=[[4,3],
          [2,1]]

mx_1.append(matrix_1)
mx_2.append(matrix_2)

matrix_suma=[]
matrix_resta=[]
mtrx_mult=[]
mtrx_div=[]


#matriz 1
print('Matriz 1: ')
for i in mx_1:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')

#matriz 2
print('Matriz 2: ')
for i in mx_2:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')

#suma
for i in range(len(matrix_1)):
    mtrx_mas=[]
    for j in range(len(matrix_1[0])):
        mtrx_mas.append(matrix_1[i][j] + matrix_2[i][j])
    matrix_suma.append(mtrx_mas)

print('suma de mariz: ',)
for i in matrix_suma:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')

#resta
for i in range (len(matrix_1)):
    mtrx_menos=[]
    for j in range(2):
        mtrx_menos.append(matrix_1[i][j] - matrix_2[i][j])
    matrix_resta.append(mtrx_menos)

print('resta de mariz: ',)
for i in matrix_resta:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')

#producto matriz

for i in range(len(matrix_1)):
    mtrx_mult.append([])
    for j in range(len(matrix_2[0])):
        mtrx_mult[i].append(0)

for i in range(len(matrix_1)):
    for j in range(len(matrix_2[0])):
        for k in range(len(matrix_1)):
            mtrx_mult[i][j]+=matrix_1[i][k] *matrix_2[k][j]

print('producto matriz: ') 
for i in mtrx_mult:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')

mtrx_pnt=np.sum(mtrx_mult)
print('producto punto: ',mtrx_pnt)

#division de matrices
print('inversion de matriz 2: ')
matrix_2_inv=lg.inv(matrix_2)
mtrx_inv=matrix_2_inv.tolist()
print(mtrx_inv)

for i in range(len(matrix_1)):
    mtrx_div.append([])
    for j in range(len(mtrx_inv[0])):
        mtrx_div[i].append(0)

for i in range(len(matrix_1)):
    for j in range(len(mtrx_inv[0])):
        for k in range(len(matrix_1[0])):
            mtrx_div[i][j]+=matrix_1[i][k] *mtrx_inv[k][j]

print('division matriz: ') 
for i in mtrx_div:
    print('[', end=' ')
    for j in i:
        print(j, end=' ')
    print(']')