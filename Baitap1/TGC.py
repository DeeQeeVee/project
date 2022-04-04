#Create file input and output
file_input = open("TGC.inp", "r")
file_output = open("TGC.out", "w")

#Read input and convert string to number
n = file_input.read()
n = int(n)

#Create new variable
q = 0

#Calculating...
while n > 0:
        i = 1

        #Find space
        while i<n:
                print(" ", end = "", file = file_output)
                i += 1
        k = 0

        #Insert "*"
        while k <= q:
                print("*", end = "", file = file_output)
                k += 1
        n -= 1
        q += 2

        #Creat new line
        print("\n", end = "", file = file_output)