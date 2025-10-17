#!/usr/bin/env python3

# python6_obj = open("Python_06.txt", "r")
# for line in python6_obj:
#     print(line)
# python6_obj.close()

# python6_nnl = open("Python_06.txt", "r")
# for line in python6_nnl:
#     line = line.rstrip()
#     print(line)
# python6_nnl.close()

# with open("Python_06.txt","r") as python6_upper:
#     for line in python6_upper:
#         line = line.rstrip()
#         line = line.upper()
#         print(line)

# with open ("Python_06.txt","r") as python6_read, open ("Python_06_uc.txt","w") as python6_write:
#     for line in python6_read:
#         line = line.rstrip()
#         line = line.upper()
#         python6_write.write(f'{line}\n') 
#     print ("Wrote 'Python_06_uc.txt'")
 

# with open ("test.txt","r") as test_read:
#     for line in test_read:
#         test_list = line.split('\t')
#         nt_new = test_list[1].replace ('A','t').replace('T','a').replace('C','g').replace('G','c')
#         nt_new_reverse = nt_new[::-1]
#         print (nt_new_reverse) 
#         print(f'{test_list[0]},{nt_new_reverse}')


# count = 0
# with open ('Python_06.fastq.txt','r') as python6_read2:
#     for line in python6_read2:
#         if line.startswith('@'):
#             count += 1
#             print(count)

count = 0
with open ('Python_06.fastq_test.txt','r') as python6_read2:
    for line in python6_read2:
        if line.startswith('@'):
            count += 1
            print(count)



