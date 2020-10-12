import numpy as np

def parse_line(line : str):
    line = line.replace(' ','')
    line, b = line.split('=')
    b = float(b)
    a = []
    for x in "xyz":
        if(line.count(x) == 0):
            a.append(0)
            continue
        
        term, line = line.split(x)
        if term == '': term = 1 
        elif term == '+': term = 1
        elif term == '-': term = -1
        else: term = float(term)

        a.append(term)

    return a,b 

def read_system(filename):
    A = []
    B = []

    with open(filename) as fin:
        for line in fin:
            a,b = parse_line(line)
            A.append(a)
            B.append(b)

    return A,B

A,B = read_system('./hw1/sistem.txt')

A = np.asarray(A)
B = np.asarray(B)

print(A)
print(B)

det = np.linalg.det(A)
print(det)

if(det == 0): print('Eroare: det(A) = 0!')
else:
    x = np.linalg.solve(A,B)
    print(f'x = {x[0]}')
    print(f'y = {x[1]}')
    print(f'z = {x[2]}')
