#задача 2_1
import numpy as np
import random
n=int(input("Please input quantity of lines in array "))
m=int(input("Please input quantity of columns in array "))
print("Please input data in array")
A = []

for i in range(n):
    row = input().split()

    for i in range(m):
        row[i] = int(row[i])

    A.append(row)

sum_strok=np.sum(A,axis=1)
print(f"Sum of elements at lines is {sum_strok}")
max=np.argmax(sum_strok)
print("Line index with max sum is   " + str(max))










