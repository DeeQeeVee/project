#Create new file and open it
file_input = open("HOANHAO.inp", "r")
file_output = open("HOANHAO.out", "w")

#Create new variable, insert data from file to variable and convert to number
n = file_input.readline()
n = int(n)

#Create new variable
max = 0

l = file_input.read().split()
for i in range(n):
        l[i] = int(l[i])

#Calculating...

#Create new function
def laHoanhao(x):

        #Create new variable
        total = 0

        #Find total number
        for i in range(1, x // 2 + 1):
                if (x % i == 0):
                        total += i
                        if (total > x):
                                return False
                
        #Checks if the sum is equal to a given integer to make sure it"s number perfect
        if (total == x):
                return True
        else:
                return False
#Finish function

#Check from list of variables to make sure it's number perfect
for i in range(len(l)):
        if (laHoanhao(l[i]) == True):
                max += 1

#Print the result in file
print(max, file = file_output)