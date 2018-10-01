'''
Created on Aug 31, 2018

@author: PTAMBE2
'''

import math

x=int(input('Enter value of x: '))
y=int(input('Enter value of y: '))
z=float(input('Enter value of z: '))
maxNum= max(x,y,z)

print ('The MAX value of x,y,z is:')

print (maxNum)

print ('The  square root of max num is:')
sqrtNum = (math.sqrt(maxNum))
print (int(sqrtNum))
