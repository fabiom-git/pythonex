# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:55:41 2013

----- Python -----

ex3) construct: if, while, for...

FabioM-2013
"""

# ----- WHILE

# example: Fibonacci
a, b = 0, 1         # define two vars at once
while b < 100:       # like in C: ==, !=, <=, =>
    print b
    a, b = b, a+b   # end of loop
    
    
# ----- IF
# close the lines with ':'
x = 1
if x < 0:
     x = 0
     print 'Negative changed to zero'
elif x == 0:            # else
     print 'Zero'
elif x == 1:
     print 'Single'
else:
     print 'More'       # last else statement (OPTIONAL!)
     
# ----- FOR
# for iterates within the items in a list, not like in C
print
l1=['a','auto','123',666,'casa']
for i in l1:
    print i

# in a range of number:
num=range(10)
for i in num:
    print i
    
    
# ----- BREAK statement
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else: # else belongs to for !
        # loop fell through without finding a factor
        print n, 'is a prime number'
        
        
# ----- CONTINUE
# go to the next step of FOR
for num in range(2, 10):
    if num % 2 == 0:
        print "Found an even number", num
        continue
    print "Found a number", num

# ----- PASS
# do nothing
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)