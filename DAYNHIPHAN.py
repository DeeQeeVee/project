file_input = open("DAYNHIPHAN.inp", "r")
file_output = open("DAYNHIPHAN.out", "w")

n = int(file_input.readline())
F = [0] * n

def daynhiphan(i):
    for j in range(2):

        F[i] = j

        if i == n - 1:
                print(*F, sep = "", file = file_output)
        
        else:
                daynhiphan(i + 1)

daynhiphan(0)