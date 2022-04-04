#open file input and output
file_input = open("Bai3.inp", "r")
file_output = open("Bai3.out", "w")

n = file_input.readline()
n = int(n)

#Given a string of characters s consisting of only lowercase English letters. Find the first position of a character that occurs only once in s. If there are no characters that satisfy the requirements of the problem, print -1.
for line in file_input:
        line = line.strip()
        for i in range(len(line)):
                if(line.count(line[i]) == 1):
                        print(i+1, file = file_output)
                        break
        else:
                print(-1, file = file_output)