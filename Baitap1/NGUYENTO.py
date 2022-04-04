#Create new file and open it
file_input = open("NGUYENTO.inp", "r")
file_output = open("NGUYENTO.out", "w")

#Create new variable, insert data from file to variable and convert it to number
n = file_input.read()
n = int(n)

#Calculating...
#Create new function. New function will check if variable is prime
def isPrime(n):

        #If n is less than 2 then check for False
        if (n < 2):
                return "KHONGNGUYENTO"
        
        #Import function
        import math

        #Create new variables and assign them 2
        i = 2

        #If n is divisible by any number, return Fasle
        while i <= math.sqrt(n):
                if (n % i == 0):
                        return "KHONGNGUYENTO"
                i+=1

        #Otherwise returns True
        return "NGUYENTO"

#Finish the calculation and print the result to a file
print(isPrime(n), file = file_output)