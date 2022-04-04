#open file
file_input = open("DAUGIA.inp", "r")
file_output = open("DAUGIA.out", "w")

#read a, b elements from file input
a, b = map(int, file_input.readline().split())

f_list = [1] * (b +1)
count = 0

b_m = int(b**0.5)
f_list[0], f_list[1] = 0, 0

for i in range(2, b):
        if (i <= b_m):

                if (f_list[i] == 1):
                        for j in range(i**2, b  + 1, i):
                                f_list[j] = 0

        if (f_list[i] == 1) and (str(i) == str(i)[::-1]) and a <= i <= b:
                count += 1

#print count to file outpout
print(count, file = file_output)