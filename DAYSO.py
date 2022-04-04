from itertools import count


file_input = open("DAYSO.inp", "r")
file_output = open("DAYSO.out", "w")

n = file_input.readline()
a = file_input.readline().split()
for i in range(len(a)):
    a[i] = int(a[i])

n = int(n)
s = []
io = []
jo = []

def taomangs():
    count = 0
    for i in range(n + 1):
        for j in range(i + 1, n):
            count += 1
            s[count] = a[i] + a[j]
            io[count] = i
            jo[count] = j
    
    
taomangs()

def check(p):
    global count
    sp = a[p] * 3
    ktt = False

    for i in range(1, n + 1):
        spp = sp - a[i]
        for j in range(count + 1):
            if s[j] >= spp:
                break
            if s[j] == spp and io[j] != p and jo[j] != p:
                ktt = True  
    return ktt

count1 = 0
for p in range(1, n + 1):
    if check(p):
        count1 += 1
print(count1, file = file_output)