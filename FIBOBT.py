file_input = open("FIBOBT.inp", "r")
file_output = open("FIBOBT.out", "w")

n= int(file_input.read())

def ql(n):
    if n == 0 or n == 1:
        return n
    return ql(n-1) + ql(n-2)

print(ql(n), file=file_output)

file_input.close()
file_output.close()