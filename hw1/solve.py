def read_system_old(filename):
    A = []
    B = []

    with open(filename) as fin:
        for line in fin:
            line = line.replace(" ","").replace("=","")
            line = line.replace("x"," ").replace("y"," ").replace("z"," ")
            #print(line)
            nums = line.split()
            nums = [float(n) for n in nums]
            A.append(nums[:3])
            B.append(nums[3])

    return A,B

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

def det3(mat):
    s = 0
    s += mat[0][0]*mat[1][1]*mat[2][2]
    s += mat[0][1]*mat[1][2]*mat[2][0] 
    s += mat[0][2]*mat[1][0]*mat[2][1] 
    s -= mat[0][2]*mat[1][1]*mat[2][0] 
    s -= mat[0][0]*mat[1][2]*mat[2][1] 
    s -= mat[0][1]*mat[1][0]*mat[2][2] 
    return s

def det2(mat):
    return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0] 

def transpose(mat,rows=3,cols=3):
    trans = [[0 for i in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            trans[i][j] = mat[j][i]

    return trans

def star(trans):
    st = [[0 for j in range(3)] for i in range(3)]

    for i in range(3):
        for j in range(3):
            minor = []
            for ii in range(3):
                if ii == i: continue
                min_row = [trans[ii][jj] for jj in range(3) if j!=jj]
                minor.append(min_row)            
            st[i][j] = (-1)**(i+j)*det2(minor)

    return st

def scalar(mat,vec):

    result = []

    for line in mat:
        if(len(line)!=len(vec)): 
            result.append(None)
        else:
            s = 0
            for i in range(len(vec)):
                s += line[i]*vec[i]
            result.append(s)

    return result

A,B = read_system("./hw1/sistem.txt")

print(A)
detA = det3(A)
print(f"detA = {detA}")
if(detA == 0): print("Determinantul sistemului este 0!")
else:
    Atrans = transpose(A)
    #print(Atrans)
    Astar = star(Atrans)
    #print(Astar)
    Ainv = [[Astar[i][j]/detA for j in range(3)] for i in range(3)]
    #print(Ainv)
    xyz = scalar(Ainv,B)
    #print(xyz)
    print(f"x = {xyz[0]}")
    print(f"y = {xyz[1]}")
    print(f"z = {xyz[2]}")
