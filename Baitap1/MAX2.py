#Create new file and open it
file_input = open("MAX2.inp", "r")
file_output = open("MAX2.out", "w")

#Create new variables and insert data from file to variable
n = file_input.readline()
l = file_input.readline().split()

#Calculating...

#Convert variable in list to string
for i in range(len(l)):
        l[i] = int(l[i])

#Get new list is similar to original and sort it
l1 = l[::]
l1.sort()

#Get index of Second largest in the list and write it to file
print(l.index(l1[-2]) + 1, file = file_output)