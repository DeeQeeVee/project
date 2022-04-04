file_input = open("KITU.inp", "r")
file_output = open("KITU.out", "w")

S = file_input.read()
X = set(S)
x1 = {}

for i in X:
        x1[i] = 0

to = -1
ch = "A"

for i in S:
        x1[i] += 1

        if x1[i] > to:
                to = x1[i]
                ch = i

        elif (x1[i] == to) and (i < ch):
                ch = i

len = len(X)

print(len, file = file_output)
print(ch, to, file = file_output)