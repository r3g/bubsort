#!/usr/bin/env python

import csv

with open('biglist','r') as f:
  for line in f: 
    ncol = len(line.split(':'))
    word = line.split(':')[0]
    print("{0} {1}".format(word, ncol))
