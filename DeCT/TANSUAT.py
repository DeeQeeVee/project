file_input = open("TANSUAT.inp", "r")
file_output = open("TANSUAT.out", "w")

a1 = list(map(int, file_input.read().split()))
n = int(max(a1))
F = [True]*(n + 1)
F[0], F[1] = False, False
can_n = int(n**0.5) + 1 

for i in range(2, can_n + 1): 
    if F[i]:           
        for j in range(i*i, n + 1, i):
            F[j] = False 

F1 = [0]*(max(a1) + 1)

for i in a1:
    if F[i] == True:
        F1[i] += 1

max1 = 0
max2 = 0
for i in range(len(F1)):
    if F1[i] == 0:
        pass
    else:
        if F1[i] >= max1:
            max1 = F1[i]
            max2 = i

print(max2, max1, file = file_output)