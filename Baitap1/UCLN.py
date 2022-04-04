#Create new file and open it
file_input = open("UCLN.inp", "r")
file_output = open("UCLN.out", "w")

#Create new variables, read the file and write it to variable
d = file_input.read().split()
a = int(d[0])
b = int(d[1])

#Calculating...

#Create a function to calculate the greatest common divisor (GCD) of two variables
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

#Finish the calculation
#Print the greatest common divisor to file
print(GCD(a, b), file = file_output)