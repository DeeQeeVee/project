#open file input and output
file_input = open("Bai1.inp", "r")
file_output = open("Bai1.out", "w")

n = file_input.readline()
#read list of list in file input
l = []
for line in file_input:
        l.append(line.split())

total = []

#convert string to int in list input
for i in range(len(l)):
        for j in range(len(l[i])):
                l[i][j] = int(l[i][j])

#go to all cells (i,j) where the sum of numbers on row i and sum of numbers on column j are equal, write to file bai1.out a single line is the number of cells (i,j) that satisfy ask for a topic
for i in range(len(l)):
        for j in range(len(l[i])):
                sum_i = 0
                sum_j = 0
                for k in range(len(l[i])):
                        sum_i += l[i][k]
                for k in range(len(l)):
                        sum_j += l[k][j]
                if(sum_i == sum_j):
                        total.append(str(i+1) + " " + str(j+1))

#print number of elements in total
print(len(total), file = file_output)
