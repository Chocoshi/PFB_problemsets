#!/usr/bin/env python3

import re

# with open ("Python_07_nobody.txt","r") as P7nobody_read:
#     for line in P7nobody_read:
#         print(re.search(r'Nobody', line) )
       
# with open ("Python_07_nobody.txt","r") as P7nobody_read:
#     for line in P7nobody_read:
#         for var1 in re.finditer(r"Nobody", line):
#             print (var1.start(0)+1)

# with open ("Python_07_nobody.txt","r") as P7nobody_read:
#     var2 = re.findall(r'Nobody', P7nobody_read.read())
#     print(len(var2))

# with open ("Python_07_nobody.txt","r") as P7nobody_read:
#     var2 = re.findall(r'Nobody', P7nobody_read.read())
#     print(var2.count('Nobody'))

with open ("Python_07_nobody.txt","r") as P7nobody_read:
    for line in P7nobody_read:
        print(line.replace('Nobody','Loopy'))
        



        
        
          