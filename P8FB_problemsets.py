#!/usr/bin/env python3

import re
import sys

with open ("Python_08.fasta.txt", "r") as python_08_fasta:
    line_append = ''
    dict_per_gene = {}
    gene_name = ''
    for line in python_08_fasta:
        if line.startswith(">"):
            gene_name = re.findall(r"\>\S+", line)[0]
            line_append = ''
        else:
            line = line.rstrip()
            line_append += line
        dict_per_gene[gene_name] = {} #Need to build the dictionary first before filling it in.
        dict_per_gene[gene_name]['A'] = line_append.count('A')
        dict_per_gene[gene_name]['C'] = line_append.count('C')
        dict_per_gene[gene_name]['T'] = line_append.count('T')
        dict_per_gene[gene_name]['G'] = line_append.count('G')
for gene_name in dict_per_gene:
    seqName = dict_per_gene[gene_name]
    A_count = dict_per_gene[gene_name]['A']
    C_count = dict_per_gene[gene_name]['C']
    T_count = dict_per_gene[gene_name]['T']
    G_count = dict_per_gene[gene_name]['G']
    
    print(f'{gene_name}\t{A_count}\t{T_count}\t{G_count}\t{C_count}')