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

# with open ("Python_07_nobody.txt","r") as P7nobody_read:
#     for line in P7nobody_read:
#         var2 = line.replace('Nobody','Loopy')
#         print (var2)

# with open ("Python_07.fasta.txt","r") as P7fasta_read:
#     for line in P7fasta_read:
#         var3 = re.search(r"^\>\S+\s+.+$", line)
#         print(var3)


# with open ("Python_07.fasta.txt","r") as P7fasta_read:
#     for line in P7fasta_read: 
#         line = line.rstrip()
#         for found in re.finditer(r"(^\>\S+)(\s+.+$)", line):
#             print(f'id:{found.group(1)} desc:{found.group(2)}')

# with open ("Python_07.fasta.txt","r") as P7fasta_read:
#     for line in P7fasta_read: 
#         line = line.rstrip()
#         for found in re.finditer(r"(^[ACTG]*)", line):
#             print(f'seq:{found.group(1)}')

dictionary = {}
with open ("Python_07.fasta.txt","r") as P7fasta_read:
    #file = P7fasta_read.read()
    for line in P7fasta_read:
        line = line.rstrip()
        if line.startswith(">"):
            for match in re.finditer(r"(^\>\S+)", line):
                id = match.group(0)
                dictionary[id] = ''
        else:
            dictionary[id] += line
print(dictionary)
   
  

        



        
        
          