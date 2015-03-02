#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" filters a fasta file, given fasta headers

USAGE:
    fastaget.py inputfile.fa list_of_ids.txt

This generates a fasta file that contains only the entries that
are contaiend in list_of_ids.txt
"""

from Bio import SeqIO
import sys
from lib.read_results import *

filename = sys.argv[1]
filter_file = sys.argv[2]
filter_ids = read_to_dict(filter_file)

with open(filename, 'r') as f:
    read = False
    while True:
        line = f.readline()
        if line == "":
            break
        if line.startswith(">"):
            header = line[1:].split()[0].strip().lower()
            if filter_ids.get(header) is None:
                read = False
            else:
                read = True
                sys.stdout.write(line)
        elif read:
            sys.stdout.write(line)

