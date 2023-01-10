import numpy as np
# #NumPy is a library provides  various derived objects (such as masked arrays and matrices),
# #and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting,
# #I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation. 
import pandas as pd 
import sympy as sp
from sympy import *
# # CALCULATION OPERATION:  +, -, *, /, ==, !=, 
# # LOGIC OPERATION: and, or 
# #I  DATA TYPE 
# #  1. Array  
# a = np.array([1, 2 , 3 , 4])
# b = np.array([2, 3 , 4 , 5]) 
# # Element of array 
# print(a[1])
# print(a + b) 
# print(a * b) 
# print(a / b)  
# print(sum(a))
# print(max(a))
# # 2. Matrix 
# mat = np.matrix([[1, 2, 3, 4], [2, 3, 4, 5]])
# mat2 = np.matrix([[1, 0, 3, 4], [2, 4, 4, 5]])
# print(np.matrix.transpose(mat2)) #transpose matrix 
# print(mat)
# print(mat + mat2) #sum of matrix 
# # Element of matrix 
# print(mat[0,0])
# print(np.matrix.max(mat))
# print(np.matrix.min(mat))
# print(np.matrix.sum(mat))
# # 3. List 
# list = [1, "2", 2, [1, 2, 3, 5]]
# print(list)
# print(list[3])
# #4.  Dataframe
# data = {'Val1' : ['1', '2', '3', '4', '5'], 
# 'Val2' : [2, 3, 4, 5, 6] }
# df = pd.DataFrame(data) 
# # Element of dataframe 
# print(df)
# print(df.iloc[0,1])
# # CONDITION
# if (max(a) > 1):
#     print("Max of array is greater than 1")
# elif (max(a) == 1):
#     print("Max of array is equal 1")
# else:
#     print("Max of array is less than 1")
# # LOOP 
# for i in range(10):
#     print(i)
# i = 1
# while i <= 10:
#     print (i)
#     i = i + 1 
# # FUNCTION  
# def func():
#     print("Hello world!")
# func()
# def bot(x):
#     if (max(a) > 1):
#         print("Max of array is greater than 1")
#     elif (max(a) == 1):
#         print("Max of array is equal 1")
#     else:
#         print("Max of array is less than 1")
# bot(b)
## 5. Input variable from user
#input = input("Enter your name: \n")
#print("Your name is", input) 
#data = {'Val1' : ['1', '2', '3', '4', '5'], 'Val2' : [2, 3, 4, 5, 6] }
#data = pd.DataFrame(data)
#print (data.describe(include='all'))
## 6. Gradient descent 
#x = Symbol('x')
#y = Symbol('y')
#f = 2*x**2+3
#g  = 2*x**2 + 3*y**3 + 2 
#f_prime = f.diff(x)
#g_prime = g.diff(y)
#print(f_prime)
#print(g_prime)
#f = lambdify(x, f)
#print(f(2))
def gradient_desc(x,f, init,lr):
    x = Symbol('x')
    f_prime = f.diff(x)
    f = lambdify(x, f)
    ext = init 
    lst = []
    for i in range(1000):
     if (f(ext) >= 0.0001):
        ext = ext - lr*f(ext)
        lst.append(ext)
     else:
        print("Extreme value of function f(x) is:", ext)
        print("Array of extreme value is:", lst)
x = Symbol('x')
f = 2*x**2+3
gradient_desc(x,f,-0.5,0.01)


