#open file input and output
file_input = open("Bai4.inp", "r")
file_output = open("Bai4.out", "w")

#read input
n, k = file_input.readline().split()
n, k = int(n), int(k)

#read data from file input
data = []
for i in range(n):
        data.append(file_input.readline().split())

#convert data to int
for i in range(n):
        for j in range(n):
                data[i][j] = int(data[i][j])
max = -99999999
# select a sub-square of size k*k whose sum of the values of all the cells of the sub-square is the largest and print a single line with a positive integer that is the sum of the maximum values required to output
for i in range(n):
        for j in range(n):
                if i + k <= n and j + k <= n:
                        sum = 0
                        for x in range(i, i + k):
                                for y in range(j, j + k):
                                        sum += data[x][y]
                        if sum > max:
                                max = sum
                                x_max = i
                                y_max = j

print(max, file = file_output)