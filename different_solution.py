#Write a script that sorts a list of tuples based on the number value in the tuple.
#For example:
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6), ('fifth_element', 8), ('sixth_element', 10), ('seventh_element', 1), ('eight_element', 56), ('nineth_element', 15), ('tenth_element', 25), ('eleven_element', 31000)]
#sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

#Empty lists
sorted_list = []
sorted_list2 = []

#Lenght of unsorted_list == 5
lastlst = len(unsorted_list)
#Lenght of unsorted_list - 1 == 4
x = lastlst - 1

#Find last element in unsorted_list. Means 5 - 1 == 4 which lids to ('sixth_element', 3)
lastelemt = unsorted_list[x]

#Show what is inside ('sixth_element', 3) on index 1 == number 3
value = lastelemt[1]

for i in unsorted_list:
    x = x - 1
    lastelemt = unsorted_list[x]
    value = lastelemt[1]
    value2 = lastelemt[0]
    sorted_list.insert(0, value)
    sorted_list2.insert(0, value2)
    zipped = zip(sorted_list, sorted_list2)
    lst = list(zipped)
    lst.sort()
#print(lst)

for x in range(0, len(lst) - 0): # Go until second to last tuple, because we don't need to modify last tuple
    lst[x] = (lst[x][1], lst[x][0]) # Set tuple at current location to the first element of the current tuple and the first element of the next tuple
print(lst)