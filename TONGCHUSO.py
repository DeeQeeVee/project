file_input = open("TONGCHUSO.inp", "r")
file_output = open("TONGCHUSO.out", "w")

n = file_input.readline().strip("\n")
s = str(n)

count = 0

for i in s:
        count += int(i)

print(count, file = file_output, end = "")