# This code is for computing frequency matrix
# and analyzing them.

#Type dna as you want.
dna_list = ['GGTAAAAAG', 'GGTTAC', 'GGTTGC']

# Type--1--Separate frequency lists
def freq_lists(dna_list):
    n = len(dna_list[0])
    A = [0]*n
    T = [0]*n
    G = [0]*n
    C = [0]*n
    for dna in dna_list:
        for index, base in enumerate(dna):
            if base == 'A':
                A[index] += 1
            elif base == 'C':
                C[index] += 1
            elif base == 'G':
                G[index] += 1
            elif base == 'T':
                T[index] += 1
    return A, C, G, T
A, C, G, T = freq_lists(dna_list)
print('Type-1 Frequency matrix')
print(A)
print(C)
print(G)
print(T)


# Type--2--Nested List
def freq_list_of_lists_v1(dna_list):
    # Create empty frequency_matrix[i][j] = 0
    # i=0,1,2,3 corresponds to A,T,G,C
    # j=0,...,length of dna_list[0]
    frequency_matrix = [[0 for v in dna_list[0]] for x in 'ACGT']

    for dna in dna_list:
      for index, base in enumerate(dna):
          if base == 'A':
              frequency_matrix[0][index] +=1
          elif base == 'C':
              frequency_matrix[1][index] +=1
          elif base == 'G':
              frequency_matrix[2][index] +=1
          elif base == 'T':
              frequency_matrix[3][index] +=1
    return frequency_matrix
frequency_matrix = freq_list_of_lists_v1(dna_list)
print('Type-2 Frequency matrix')
print(frequency_matrix)


# Iype--3--Using dictionary for indexing
def freq_list_of_lists_v2(dna_list):
    frequency_matrix = [[0 for v in dna_list[0]] for x in 'ACGT']
    base2index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    for dna in dna_list:
        for index, base in enumerate(dna):
            frequency_matrix[base2index[base]][index] += 1
    return frequency_matrix
frequency_matrix2 = freq_list_of_lists_v2(dna_list)
print('Type-3 Frequency matrix')
print (frequency_matrix2)


# Type--4-- Using numerical python
import numpy as np
def freq_numpy(dna_list):
    frequency_matrix = np.zeros((4, len(dna_list[0])), dtype=np.int)
    base2index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    for dna in dna_list:
        for index, base in enumerate(dna):
            frequency_matrix[base2index[base]][index] += 1
    return frequency_matrix
frequency_matrix = freq_numpy(dna_list)
print('Type-4 Frequency matrix')
print (frequency_matrix)


# Type--5--Using Dictionary of lists
def freq_dict_of_lists_v1(dna_list):
    n = max([len(dna) for dna in dna_list])
    frequency_matrix = {
        'A': [0]*n,
        'C': [0]*n,
        'G': [0]*n,
        'T': [0]*n,
        }
    for dna in dna_list:
        for index, base in enumerate(dna):
            frequency_matrix[base][index] += 1
    return frequency_matrix
frequency_matrix = freq_dict_of_lists_v1(dna_list)
print('Type-5 Frequency matrix')
import pprint; pprint.pprint(frequency_matrix)


# Type--6--Using Dictionary of dictionaries
def freq_dict_of_dicts_v1(dna_list):
    n = max([len(dna) for dna in dna_list])
    frequency_matrix = {base: {index: 0 for index in range(n)}
                        for base in 'ACGT'}
    for dna in dna_list:
        for index, base in enumerate(dna):
            frequency_matrix[base][index] += 1
    return frequency_matrix
frequency_matrix = freq_dict_of_dicts_v1(dna_list)
print('Type-6 Frequency matrix')
print (frequency_matrix)


# Type--7--Using Dictionaries with defult value
from collections import defaultdict
def freq_dict_of_dicts_v2(dna_list):
    n = max([len(dna) for dna in dna_list])
    frequency_matrix = {base: defaultdict(lambda: 0)
                        for base in 'ACGT'}
    for dna in dna_list:
        for index, base in enumerate(dna):
            frequency_matrix[base][index] += 1
    return frequency_matrix
frequency_matrix = freq_dict_of_dicts_v2(dna_list)
print('Type-7 Frequency matrix')
print (frequency_matrix)


# Analyzing frequency frequency matriix
def find_consensus_v3(frequency_matrix):
    if isinstance(frequency_matrix, dict) and \
       isinstance(frequency_matrix['A'], dict):
        pass # right type
    else:
        raise TypeError('frequency_matrix must be dict of dicts')

    consensus = ''
    dna_length = len(frequency_matrix['A'])

    for i in range(dna_length):  # loop over positions in string
        max_freq = -1            # holds the max freq. for this i
        max_freq_base = None     # holds the corresponding base

        for base in 'ACGT':
            if frequency_matrix[base][i] > max_freq:
                max_freq = frequency_matrix[base][i]
                max_freq_base = base
            elif frequency_matrix[base][i] == max_freq:
                max_freq_base = '-' # more than one base as max

        consensus += max_freq_base  # add new base with max freq
    return consensus
frequency_matrix = freq_dict_of_dicts_v1(dna_list)
print ('Analyzed result','=',find_consensus_v3(frequency_matrix))



