# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:56:10 2019
@author: tony.ding
"""
from itertools import permutations
n = 8
cols = range(n)
for vec in permutations(cols):
    if (n == len(set(vec[i]+i for i in cols))
          == len(set(vec[i]-i for i in cols))):
        print (vec)
        print ("\n".join('.' * i + 'Q' + '.' * (n-i-1) for i in vec), end = "\n===\n")
        

# =============================================================================
# from itertools import permutations
# for vector in permutations(reversed(range(8))):
#     if len(set(vector[index] + index for index in range(8))) == len(set(vector[index] - index for index in range(8))) == 8:
#         print('\n'.join('- ' * index + 'Q ' + '- ' * (7 - index) for index in vector), end='\n\n')
# =============================================================================
