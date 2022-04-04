#open file input and output
file_input = open("Bai2.inp", "r")
file_output = open("Bai2.out", "w")

#read string in file input
s = file_input.readline()

#create a list
total = []

for i in s:
        if i in ["2", "3", "5", "7"]:
                total.append(i)

#delete duplicate in list total
total = list(dict.fromkeys(total))


#write string in file output
file_output.write(" ".join(total))