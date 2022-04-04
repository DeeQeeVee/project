file_input = open("GTQHD.inp", "r")
file_output = open("GTQHD.out", "w")

n= int(file_input.read())

def qhd(n):
    a =[1]*(n+1)
    for i in range(2,n+1):
        a[i] = a[i-1]*i
    return a[n]

print(qhd(n), file = file_output)

file_input.close()
file_output.close()