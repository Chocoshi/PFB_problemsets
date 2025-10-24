#!/usr/bin/env python3

import sys, re, os

field_colnames = "qseqid, sseqid, percid, alen, mismat, gaps, q_start, q_end, s_start, s_end, evalue, bits"
fields = field_colnames.split(', ')

row_dict = []
final_list = []
for specific_file in sys.argv[1:]:
    with open(specific_file,"r") as search_result:
        for line in search_result:
            line = line.rstrip()
            if not line.startswith("#"):
                column_lists = line.split('\t')
                row_dict = dict(zip(fields, column_lists))
                final_list.append(row_dict)

for dict_line in final_list:  
    print(dict_line["percid"], dict_line["alen"], dict_line["evalue"])


# column_lists.insert(0, field_colnames)

# five_list.append(column_lists)

                




    

