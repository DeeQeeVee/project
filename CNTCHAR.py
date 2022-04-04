file_input = open("CNTCHAR.inp", "r")
file_output = open("CNTCHAR.out", "w")

S = file_input.readline().lower()
F = {}

for i in S:
        if i not in F:
                F[i] = 1

        else:
                F[i] += 1

F = dict(sorted(F.items()))
print(F)

for i in F:
        print(i, F[i], sep = ":", file = file_output)