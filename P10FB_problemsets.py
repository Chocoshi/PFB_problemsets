#!/usr/bin/env python3

import re 

# def per60lines(dna):
#     per60lines_str = re.sub(r'(\w{60})', r'\1\n', dna)
#     return per60lines_str

# dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'

# outputP10q1 = per60lines(dna)
# print(outputP10q1)

# dna2 = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
# GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
# CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
# TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
# TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
# CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
# GTCATCTTCT'''


# outputP10q2 = dna2.split("\n")
# separator = ''
# joined_outputP10q2 = separator.join(outputP10q2)
# print(joined_outputP10q2)

# for i in range(0,len(joined_outputP10q2),60):
#     print(joined_outputP10q2[i:i+60])


# def two_arguments(dna1, width):
#     var3 = ''
#     for i in range(0,len(dna1),width):
#         var3 += dna1[i:i+width] + "\n"
#     return var3

# dna1 = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
# width = 80

# print(two_arguments(dna1,width))

import sys

# def two_command_arguments(fasta_filename, max_line_length):
#     with open (fasta_filename, "r") as read1:
#         var3 = ''
#         total_seq = ''
#         max_line_length = int(max_line_length)
#         for line in read1:
#             line = line.rstrip() 
#             total_seq += line
#         for i in range(0,len(total_seq),max_line_length):
#             var3 += total_seq[i:i+max_line_length] + "\n"
#     return var3

# fasta_filename = sys.argv[1]
# max_line_length = sys.argv[2]

# print(two_command_arguments(fasta_filename, max_line_length))

def two_command_line(fasta_filename, max_line_length):
    with open (fasta_filename, "r") as read1:
        total_seq = ''
        total_seq2 = ''
        max_line_length = int(max_line_length)
        for line in read1:
            line = line.rstrip() 
            total_seq += line
        for i in range(0,len(total_seq),max_line_length):
            total_seq2 += total_seq[i:i+max_line_length] + "\n"
    return total_seq2

fasta_filename = sys.argv[1]
max_line_length = sys.argv[2]

print(two_command_line(fasta_filename, max_line_length))

#Created a file named fasta.test.txt that has contains the INPUT from P10q3.

