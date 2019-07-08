# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:22:10 2019

@author: SHAIL
"""
abcd = ['nintendo','Spain', 1, 2, 3]


# Ex1 - Select the third element of the list and print it
print(abcd[2])




# Ex2 - Type a nested list with the follwing list elements inside list abcd mentioned above and print it

newlist = ['nintendo', [54,76], 'Spain', 1, 2, 3]
print(newlist)


# Ex3 - Print the 1 and the 4 position element in the following list

nestedlist = ["shail", [11,8, 4, 6], ['toronto'],abcd, "abcd"]
a = nestedlist[1]
b = nestedlist[4]
print(a)
print(b)


# Ex4  - add the fllowing 2 lists and create list3 and print 

list1= [10, 20, 'company', 40, 50, 100]

list2 = [100, 200, 300, 'orange', 400, 500,1000]

list3 = list1 + list2
print(list3)


# Ex 5 - print the lenght of the list3
print(len(list3))




# Ex 6 Add 320 to list 1 and print
list4.append(320)
print(list4)

#Ex 7 - Add parts of list1 & 2 by tking first 4 elements from list1 and last 2 elements from list2
a = list1[:4]
b = list2[2:]
ab = a + b
print(ab)


#ex 8 check if 99 is in list 1 
print(list1.count('99'))

#ex 9 check if 99 is not in list 1 
99 not in list1



# concatenation (+) and replication (*) operators
#ex 10 - CONCATENANTE  list 1 and ['cool', 1990]
conc = list1
conc2 = ['cool', '1990']
concac = conc + conc2
print(concac)
# Ex 11 -  triplicate the list 1
trip = list1 * 3
print(trip)


list2 = [100, 200, 300, 400, 500,1000]

# ex 12 - find min & max of list2
maxnum = max(list2)
max(maxnum)
minnum = max(list2)
min(minnum)
print(minnum)
# append & del
# Ex 13 append 'training' to list 1
list1.append('training')

# Ex 14 delete 2nd position element from list 2
del list2[2]


# Ex 15 - iterate over list1 and print all elements by adding 10 to each element

list1= [10, 65,20, 30,93,  40, 50, 100]

for x in list1:
    print(x + 10)

# for x in list1:
    


#Ex 16 sorting

#sort list1 by ascending order
list1.sort()



#sort list1 by reverse order
list1.reverse()
print(list1)    

