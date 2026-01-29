#!/usr/bin/python3
import re

def calc(A, B):
    if isinstance(A, str):
        if not re.fullmatch(r'\d+', A):
            return -1
        A = int(A)
        
    if isinstance(B, str):
        if not re.fullmatch(r'\d+', B):
            return -1
        B = int(B)

    if isinstance(A, int) and isinstance(B, int):
        if 1 <= A <= 999 and 1 <= B <= 999:
            return A * B
            
    return -1

def main():
    while True:
        try:
            line = input('input A: ')
            if line == 'end': break
            A = line
            line = input('input B: ')
            if line == 'end': break
            B = line
            print('input A * input B = ', calc(A, B))
        except EOFError:
            break

if __name__ == '__main__':
    main()