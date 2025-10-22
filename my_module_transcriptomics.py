#!/usr/bin/env python3

import os, sys, re

from collections import Counter

## method: seq_list_from_fastq_file(fastq_filename)
##
##  Extracts the sequence lines from a fastq file and returns a list
##  of the sequence lines
##
##  input parameters:
##
##  fastq_filename :  name of the fastq file (type: string)
##
##  returns seq_list : list of read sequences.
##                    ie.  ["GATCGCATAG", "CGATGCAG", ...]

from Bio import SeqIO


def seq_list_from_fastq_file(fastq_filename):
    seq_list = []
    for seq_record in SeqIO.parse(fastq_filename,"fastq"):
        sequence_transcriptome = str(seq_record.seq)
        seq_list.append(sequence_transcriptome) 
    return seq_list


def main():

    progname = sys.argv[0]
    
    usage = "\n\n\tusage: {} filename.fastq num_seqs_show\n\n\n".format(progname)
    
    if len(sys.argv) < 3:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    num_seqs_show = int(sys.argv[2])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    print(seq_list[0:num_seqs_show])

    sys.exit(0)  # always good practice to indicate worked ok!



def sequence_to_kmer_list(fastq_filename, kmer_length):

    for seq_record in SeqIO.parse(fastq_filename,"fastq"):
        seq_list = []
        kmer_list = []
        sequence_transcriptome = str(seq_record.seq)
        seq_list.append(sequence_transcriptome) 
        for start_position in range(len(sequence_transcriptome)):
            kmer_sequence = sequence_transcriptome[start_position:start_position+kmer_length]
            if len(kmer_sequence) == kmer_length:
                kmer_list.append(kmer_sequence)
    return kmer_list
            
# print(sequence_to_kmer_list(sys.argv[1], int(sys.argv[2])))

def count_kmers(kmer_list):
    return Counter(kmer_list)

    # print(count_kmers('kmerlist.txt'))

if __name__ == '__main__':
    main()