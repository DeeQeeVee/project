#Create new file and open it
file_input = open("DOIXUNG.inp", "r")
file_output = open("DOIXUNG.out", "w")

#Create new variable and insert data from file to variable
s = file_input.read()

#Calculating...

#Finish the calculation and print the results to a file
if (s[::-1] == s):
        print("DOIXUNG", file = file_output)
else:
        print("KHONGDOIXUNG", file = file_output)