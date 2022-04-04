file_input = open("FIBOQHD.inp", "r")
file_output = open("FIBOQHD.out", "w")

n= int(file_input.read())

def qhd(n):
    a =[1]*(n+1)
    for i in range(3,n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]

print(qhd(n), file=file_output)

file_input.close()
file_output.close()