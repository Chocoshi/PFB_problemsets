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

# taxa_string = 'sapiens : erectus : neanderthalensis'
# print (taxa_string)
# taxa_list = taxa_string.split(':')
# print (taxa_list)
# taxa_list.sort()
# print (taxa_list)
# taxa_list.sort (key = len)
# print (taxa_list)

# my_list = ['a','bb','ccc']
# # If you use .copy, you don't modify the original list, but if you just assign =, the original list is modified; compare my_list and my_list2.
# list_copy = my_list
# print(my_list)
# list_copy.append('ddd1')
# print(my_list)
# my_list2 = ['a','bb','ccc']
# list_copy2 = my_list2.copy()
# print(my_list2)
# list_copy2.append('ddd2')
# print(my_list2)

# number = 1
# while number < 101:
#     print("Number:", number)
#     number +=1
# print('Done')

# number = 0
# while number < 100:
#     number += 1
#     print("Number:", number)
# print('Done')

# sum = 0
# number = 0
# while number < 101:
#     sum += number 
#     number += 1
# print("Sum:", sum)

# factorial = 1
# number = 0
# while number < 10:
#     number += 1
#     factorial *= number  
# print(f'factorial: {factorial}')

# even = []
# loopy = [101,2,15,22,95,33,2,27,72,15,52]
# for num in loopy:
#     if num % 2 == 0: 
#         even.append (num)
# print (even)

# loopy.sort()
# print(loopy)


# sum = 0
# sum2 = 0
# for num in loopy:
#     print(num)
# for num in loopy:
#     if num % 2 == 0:
#         sum += num
#     else:
#         sum2 += num
# print(sum)
# print(sum2)

# problemset8_list2 = [num for num in range(100)]
# print(problemset8_list2)

# problemset8_list = [ num + 1 for num in range(100)]
# print(problemset8_list)



import sys

minimum = int(sys.argv[1])
maximum = int(sys.argv[2])

for num in range (minimum, maximum+1):
    print(num)


