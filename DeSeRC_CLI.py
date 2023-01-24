#DeSeRC
import pandas as pd
import numpy as np
import os, sys


#define function to take reverse complement of a sequence
def reverse_complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N','W':'S','S':'W', 'M':'K','K':'M','R':'Y','Y':'R','B':'V','V':'B','D':'H','H':'D'}
    bases = list(seq)
    bases = reversed([complement.get(base, base) for base in bases])
    return ''.join(bases)

#have user imput sequence
seq = input("Enter sequence: ")
print(reverse_complement(seq))
