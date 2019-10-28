# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:16:47 2019

@author: Karthik Bharadhwaj
"""

#NUMPY

import numpy as np

#one dimensional array
a = np.array([1,2,3,4],dtype="int16")
#print(a)

#two dimensional array 

b = np.array([[6.0,8.0,7.0],[3.0,2.0,1.0]],dtype='int64')

#print("two dimensional array : \n",b)


# get dimensions 

  print(a.ndim)

  print(b.ndim)

# get shape of array 

  print(a.shape)

  print(b.shape)

# get data type of array
  
print(a.dtype)

print(b.dtype)


# item size 

print(b.itemsize)

#total elements 

print(b.size)

# total size 

print(b.itemsize * b.size)

# no of bytes 

print(b.nbytes)

#Accessing  specific elements, row,column a[r, c]

a =np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])

#accessing element 10
print(a[1,3])

#accessing element 6

print(a[0,-1])

#acessing row

print(a[0,:]) # first row with all columns

# accessing columns
print(a[:,2]) #all rows with 2nd column

#array[startindex : endindex : stepsize]

print(a[0,1:6:2]) #[2,4,6]


#print 9,10,11
print(a[1,2:5])

#changing values 

a[0,5]=66

a[1,5] =122
print(a)

a[:,2] =[6,3]

print(a)

#3D array
b =np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(b)

#print(b[0,1,0])

b[1,:,1:] =[[6,3],[3,6]]

print(b)

#zeros matrices
z = np.zeros([3,2,2])

#print(z)

#ones matrices

o = np.ones([6,3,2],dtype="int32")

#print(o)

#any different value 

d = np.full([3,2,2],23)

print(d)

v = np.full_like(b,4)

print(v)

#Random number  decimal numbers

r = np.random.rand(2,2,2)

#print(r)
#random integer number 
ri = np.random.randint(2,10,size=(4,4,4))

print(ri)

#identity

i = np.identity(4)
print(i)

#repeat an array

arr = np.array([[1,2,3]])

r = np.repeat(arr,3,axis=0) #axis = 0 ==> row and axis =1 ==> column

print(r)

one = np.ones((6,6))

print(one)


zero =np.zeros((4,4),dtype="int32")


zero[1:3,1:3]=63

one[1:5,1:5] = zero

print(one)

#LINEAR ALGEBRA 

#MatMul 
a = np.ones((3,2),dtype='int32')

print(a)

b = np.full((2,3),2)

print(b)

print(np.matmul(a,b))



#statistics 

arr = np.array([[1,2,3,4],[5,6,7,8]])


print(np.sum(arr))

#rearranging array

before = np.array([[1,2,3,4],[5,6,7,8]])

print(before)

after = before.reshape((2,2,2))

print(after)


#vertical stacking

v1 = np.array([1,2,3,4])

v2 = np.array([5,6,7,8])

v = np.vstack((v1,v2,v1))

print(v) 



#horizontal stacking

h1= np.array([1,2,3,4])

h2 = np.array([5,6,7,8])

h = np.hstack((h1,h2))

print(h)