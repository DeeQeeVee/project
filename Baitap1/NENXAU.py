#Create new file and open it
file_input = open("NENXAU.inp", "r")
file_output = open("NENXAU.out", "w")

#Create new variable and insert data from file to variable
s = file_input.read()

#Create new variable
total = ""

#Calculating...

total = s[0]
for i in range(1, len(s)):
        if s[i] != s[i - 1]:
                total += s[i]

print(total, file = file_output)