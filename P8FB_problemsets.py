#!/usr/bin/env python3

import re
import sys

# with open ("Python_08.fasta.txt", "r") as python_08_fasta:
#     line_append = ''
#     dict_per_gene = {}
#     gene_name = ''
#     for line in python_08_fasta:
#         if line.startswith(">"):
#             gene_name = re.findall(r"\>\S+", line)[0]
#             line_append = ''
#         else:
#             line = line.rstrip()
#             line_append += line
#         dict_per_gene[gene_name] = {} #Need to build the dictionary first before filling it in.
#         dict_per_gene[gene_name]['A'] = line_append.count('A')
#         dict_per_gene[gene_name]['C'] = line_append.count('C')
#         dict_per_gene[gene_name]['T'] = line_append.count('T')
#         dict_per_gene[gene_name]['G'] = line_append.count('G')
# for gene_name in dict_per_gene:
#     seqName = dict_per_gene[gene_name]
#     A_count = dict_per_gene[gene_name]['A']
#     C_count = dict_per_gene[gene_name]['C']
#     T_count = dict_per_gene[gene_name]['T']
#     G_count = dict_per_gene[gene_name]['G']
    
#     print(f'{gene_name}\t{A_count}\t{T_count}\t{G_count}\t{C_count}')

#Another way is to use finditer, when you use finditer, it spits out iterator objects, and to call the objects, you have to use a for loop and .group(0)

# with open ("Python_08.fasta.txt", "r") as python_08_fasta:
#     line_append = ''
#     dict_per_gene = {}
#     gene_name = ''
#     for line in python_08_fasta:
#         if line.startswith(">"):
#             gene_name = re.finditer(r"\>\S+", line)
#             for match in gene_name:
#                 itername = match.group(0)
#                 print(itername)

from Bio import SeqIO

# filename = "Python_08.fasta.txt"
# for seq_record in SeqIO.parse(filename,"fasta"):
#     sequence_py08 = str(seq_record.seq)
#     for codon_py08 in re.findall(r"(.{3})", sequence_py08):
#         print(codon_py08)
   
# filename = "Python_08.fasta.txt"
# for seq_record in SeqIO.parse(filename,"fasta"):
#     sequence_py08 = str(seq_record.seq)
#     for start in range(3):
#         codon_list = re.findall(r"(.{3})", sequence_py08[start:])
#         codon_string = " ".join(codon_list)
#         print(f'{seq_record.id}-frame-{start+1}-codons\n{codon_string}')

filename = "Python_08.fasta.txt"
for seq_record in SeqIO.parse(filename,"fasta"):
    sequence_py08 = str(seq_record.seq)
    reversed_sequence_py08 = sequence_py08[::-1]
    
        