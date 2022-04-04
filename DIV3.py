#open file input and output
file_input = open("DIV3.inp", "r")
file_output = open("DIV3.out", "w")

#read input
n = int(file_input.readline())

#read data in file input
demo = file_input.read().split()
data = []
for i in range(n):
        data.append(int(demo[i]))
        


s0, s1, s2 = 0, 0, 0
for i in data:

        if i % 3 == 0:
                s0 += 1

        if i % 3 == 1:
                s1 += 1

        if i % 3 == 2:
                s2 += 1
total = (s0 * (s0 - 1) / 2) + s1 * s2
print(int(total), file = file_output)