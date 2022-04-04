#Create new file and open it
file_input = open("PASCAL.inp", "r")
file_output = open("PASCAL.out", "w")

#Create new variable, insert data from file to variable and convert to number
n = file_input.read()
n = int(n)

#Calculating...

#Find the number for Pascal"s triangle
def factorial(n):
        f = 1
        while (n > 1):
                f = f * n
                n = n - 1
        return f

def ncr(n, r):
        return int(factorial(n) / (factorial(n - r) * factorial(r)))

#Finish the calculation
#Print the number for Pascal"s triangle to file
for i in range(0, n): 
        for j in range(0 , i + 1):
                print(ncr(i, j), end=" ", file = file_output) 
 
        print("", file = file_output)