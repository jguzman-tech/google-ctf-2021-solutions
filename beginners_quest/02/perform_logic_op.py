#!/usr/bin/env python3

import pandas as pd

def NOT(x):
    return not x

def AND(x, y):
    return x and y

def OR(x, y):
    return x or y

def XOR(x, y):
    return x ^ y

def NOR(x, y):
    return x == False and y == False

if __name__ == '__main__':
    data = pd.DataFrame(columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','Output'])
    for i in range(0, 2**10):
        A = i & 0x1 == 0x1
        B = i & (0x1 << 1) == 0x1 << 1
        C = i & (0x1 << 2) == 0x1 << 2
        D = i & (0x1 << 3) == 0x1 << 3
        E = i & (0x1 << 4) == 0x1 << 4
        F = i & (0x1 << 5) == 0x1 << 5
        G = i & (0x1 << 6) == 0x1 << 6
        H = i & (0x1 << 7) == 0x1 << 7
        I = i & (0x1 << 8) == 0x1 << 8
        J = i & (0x1 << 9) == 0x1 << 9
        # special bools
        # NOR: A == False and B == False
        # XOR: A ^ B
        output = AND(\
                     AND(\
                         NOR(A, NOT(B)),
                         NOR(\
                             OR(NOT(C), D),
                             OR(E, NOT(F)))),
                     AND(\
                         AND(\
                             NOR(G, H), \
                             XOR(H, I)), \
                         AND(I, J)))
        data.loc[len(data)] = [A, B, C, D, E, F, G, H, I, J, output]

    data.to_csv("truth_table.csv", index=False)

