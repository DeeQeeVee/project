#open file input and output
file_input = open("CHIADAY.inp", "r")
file_output = open("CHIADAY.out", "w")

n, l = int(file_input.readline()), list(map(int, file_input.read().split()))

l_sum = [l[0]]

for i in range(1, n):
        l_sum.append(l_sum[i - 1] + l[i])

sum_3 = 0
count = 0

if l_sum == 0:
        d = l_sum.count(0) - 2
        count = (d + 1) * d/2

elif l_sum[i] % 6 == 0:
        for i in l_sum[:n - 1]:
                if i == l_sum[n - 1] / 3:
                        sum_3 += 1
                
                if i == 2*l_sum[n - 1] / 3:
                        count += sum_3

print(int(count), file = file_output)