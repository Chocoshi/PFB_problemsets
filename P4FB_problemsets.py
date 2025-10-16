#!/usr/bin/env python3
# my_fav_list = ['chocolate', 'husband', 'kid1', 'kid2', 'bed']
# print(my_fav_list)
# print(my_fav_list[2])
# my_fav_list[2] = 'cake'
# print(my_fav_list)
# my_fav_list.append('appended')
# print(my_fav_list)
# my_fav_list.insert(0,'inserted')
# print(my_fav_list)
# my_fav_list.insert(2, 'another')
# print(my_fav_list)
# my_fav_list.pop(7)
# print(my_fav_list)
# my_fav_list.remove('bed')
# print(my_fav_list)
# new_string = ','.join(my_fav_list)
# print(new_string)

taxa_string = 'sapiens : erectus : neanderthalensis'
print (taxa_string)
taxa_list = taxa_string.split(':')
print (taxa_list)
taxa_list.sort()
print (taxa_list)
taxa_list.sort (key = len)
print (taxa_list)

my_list = ['a','bb','ccc']
# If you use .copy, you don't modify the original list, but if you just assign =, the original list is modified; compare my_list and my_list2.
list_copy = my_list
print(my_list)
list_copy.append('ddd1')
print(my_list)
my_list2 = ['a','bb','ccc']
list_copy2 = my_list2.copy()
print(my_list2)
list_copy2.append('ddd2')
print(my_list2)

