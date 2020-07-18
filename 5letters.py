# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:47:36 2019

@author: tony.ding
"""

def fiveLetters(n):
    # print("Calculating envolops of", n, " is ")
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (n - 1) * (fiveLetters(n - 1) + fiveLetters(n - 2))


print(fiveLetters(5))


def fiveLettersPemution(n):
    # print("Calculating envolops of", n, " is ")
    if n == 1:
        return 1
    else:
        return n * (fiveLettersPemution(n - 1))


print(fiveLettersPemution(5))

print((fiveLetters(5)) / (fiveLettersPemution(5)))

# =============================================================================
# def fiveLettersPossibility(n):
#     possibility = fiveLetters(5)/fiveLettersPemution(5)
# print (possibility)
# 
# =============================================================================
