#!/usr/bin/env python3
my_fav_list = ['chocolate', 'husband', 'kid1', 'kid2', 'bed']
print(my_fav_list)
print(my_fav_list[2])
my_fav_list[2] = 'cake'
print(my_fav_list)
my_fav_list.append('appended')
print(my_fav_list)
my_fav_list.insert(0,'inserted')
print(my_fav_list)
my_fav_list.insert(2, 'another')
print(my_fav_list)
my_fav_list.pop(7)
print(my_fav_list)
my_fav_list.remove('bed')
print(my_fav_list)
new_string = ','.join(my_fav_list)
print(new_string)
