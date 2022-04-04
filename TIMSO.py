file_input = open("TIMSO.inp", "r")
file_output = open("TIMSO.out", "w")

a = file_input.read().split()

A = int(a[0])
X = int(a[1])
i = 0

while A ** i <= X:
        i += 1

file_output.write(str(i - 1))