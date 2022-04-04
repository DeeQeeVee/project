file_input = open("GTBT.inp", "r")
file_output = open("GTBT.out", "w")

n= int(file_input.read())

def ql(n):
    if n == 0:
        return 1
    return n*ql(n-1)

print(ql(n), file = file_output)

file_input.close()
file_output.close()