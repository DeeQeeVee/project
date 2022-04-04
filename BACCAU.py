#open file input and output
file_input = open("BACCAU.inp", "r")
file_output = open("BACCAU.out", "w")

#input data from file input
m, n, k = file_input.readline().split()
m, n, k = int(m), int(n), int(k)

#create list of list with index of the list is the number of the line
list_of_list = []
for i in range(k):
        list_of_list.append([False] * 2)

for i in file_input:
        i = i.split()
        list_of_list[int(i[0])][int(i[1])] = True
print(list_of_list)