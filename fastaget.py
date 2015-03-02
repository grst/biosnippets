#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" retrieve a fasta sequence specified by it's identifier

USAGE:
    fastaget.py inputfile.fa header

will return
    "content of entry2"

if inputfile.fa is
    >xxx
    content of entry1
    >header
    content of entry2

"""

from Bio import SeqIO
import sys

filename = sys.argv[1]
key = sys.argv[2]

records = SeqIO.index(filename, "fasta")

try:
    print records[key].seq
except KeyError:
    print >> sys.stderr, "Key not found: " + key
