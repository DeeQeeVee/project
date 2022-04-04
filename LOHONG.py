#open file input and output
import string


file_input = open("LOHONG.inp", "r")
file_output = open("LOHONG.out", "w")

#get a element from file input
a = str(file_input.readline())

count = 0

for i in a:
        if i in ["4", "6", "9", "0"]:
                count += 1

        if i == "8":
                count += 2

#print count to file output
print(count, file = file_output)