#Create new file and open it
file_input = open("TIENDIEN.inp", "r")
file_output = open("TIENDIEN.out", "w")

#Create new variable, insert data from file to variable and convert to number
n = file_input.read()
n = int(n)

#Create new variable
total = 0

#Calculating...
if n <= 50:
        total = n * 1678

elif (n >= 51) and (n <=100):
        total = 83900 + (n - 50) * 1734

elif (n >= 101) and (n <= 200):
        total = 83900 + 86700 + (n - 100) * 2014

elif (n >= 201) and (n <= 300):
        total = 83900 + 86700 + 201400 + (n - 200) * 2536

elif (n >= 301) and (n <= 400):
        total = 83900 + 86700 + 201400 + 253600 + (n - 300) * 2834

elif (n >= 401):
        total = 83900 + 86700 + 201400 + 253600 + 283400 + (n - 400) * 2927

#Finish the calculation and print the results to a file
print(total, file = file_output)