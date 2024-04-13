# Sets
my_set = {} #create sets

#initiate set
my_set = {1,2,3,4} 
my_set2 = {5,6,7,8,9,10} 

print(my_set) # print my_set variabel
print(my_set2) # print my_set2 variabel

#manipulate sets

my_set2.add(4) # add element into set
my_set.add(5)
print(my_set)
my_set2.remove(5) #remove element from set
print(my_set2)

print(my_set.union(my_set2),'-------------',my_set|my_set2) # collab all element in one set
print(my_set.intersection(my_set2),'-------------',my_set & my_set2) # get intersection or same value between sets function
print(my_set.difference(my_set2),'---------------',my_set - my_set2) #
print(my_set.symmetric_difference(my_set2),'------------',my_set ^ my_set2) #



