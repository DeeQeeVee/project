#Create and open file input and output
file_input = open("TGV.inp", "r")
file_output = open("TGV.out", "w")

#Read input and convert string to number
n = file_input.read()
n = int(n)

#Calculating...
for i in range(1, n + 1):
        print(i * "*", file = file_output)