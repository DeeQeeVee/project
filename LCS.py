file_input = open("LCS.inp", "r")
file_output = open("LCS.out", "w")

n, m = file_input.readlines()

end_n, end_m = len(n) + 1, len(m) + 1

count_list = []
test = [0] * (end_n)

for i in range(end_m):
        count_list.append(test)

for i in range(1, end_m):
        for j in range(1, end_n):

                if n[j - 1] == m[i - 1]:
                        count_list[i][j] = count_list[i - 1][j - 1] + 1
                        
                else:
                        count_list[i][j] = max(count_list[i - 1][j], count_list[i][j - 1])

print(count_list[end_m - 1][end_n - 1], file = file_output)