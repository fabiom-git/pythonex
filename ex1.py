# ----- Python -----
# ex1) DICT and LIST datatypes
# 
# FabioM-2013   #test-git #test2

#----- DICT

dic1 = {"marca":"Fiat","modello":"Tipo 1.4 i.e"} # delimited by {}
print 'DICT is: ',dic1

print 'MARCA: ',dic1['marca']
print 'MODELLO: ', dic1['modello']
#print dic1[1] #errore


# ----- LIST

list1 = ['a','b','item3','item4',5] # delimited by []
print 'LIST is: ',list1
print list1[0]
print list1[-1]
print list1[0:3]
print list1[:3]
print list1[3:]

# append methods
list1.append('nuovo') # single item
print list1

list1.insert(2,'item2') # item at index 2
print list1

list1.append(['l1','l2','l3']) # append a list, list of list
print list1

list1.extend(['e1','e2','e3']) # append many single element
print list1

list1 + ['add1','add2'] # append 2 items without assigning
print list1 + ['add1','add2'] # repeat append

# list operation similar to Matlab
list1 = [];
list1 = ['a','b','c','d']
list1[0:2] = ['xx']*2       # double item
print list1


ll=[('*')*10]*10
tt=(('*')*10)*10
tt=('*')*100
