file_input = open("timso.inp", "r")
file_output = open("timso.out", "w")
A, X = file_input.read().split()
A, X = int(A), int(X)
i = 0
while A**(i+1) <= X:
    i += 1
print(i, file=file_output)
file_input.close()
file_output.close()
