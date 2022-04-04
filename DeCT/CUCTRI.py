file_input = open("CUCTRI.inp", "r")
file_output = open("CUCTRI.out", "w")

l1 = file_input.readline().split()
n, m = int(l1[0]), int(l1[1])

l2 = []
for i in range(n):
        l3 = list(map(int, file_input.readline().split()))
        l2.append(l3)

max_l2 = [ [99999]*(n + 2), [99999]*(n + 2) ]
min_l2 = [ [-99999]*(n + 2), [-99999]*(n + 2) ]

for i in range(n):
        l2[i].insert(0, 99999)
        l2[i].append(99999)

        max_l2.insert(i + 1, l2[i].copy())
        l2[i][0], l2[i][n + 1] = -99999, -99999

        min_l2.insert(i + 1, l2[i])

count = 0

for i in range(1, n + 1):

        for j in range(1, m + 1):

                if ( max_l2[i][j] > max( [min_l2[i - 1][j - 1], min_l2[i - 1][j], min_l2[i - 1][j + 1], min_l2[i][j - 1], min_l2[i][j + 1], min_l2[i + 1][j - 1], min_l2[i + 1][j], min_l2[i + 1][j + 1] ] ) or\
                        max_l2[i][j] < min( [max_l2[i - 1][j - 1], max_l2[i - 1][j], max_l2[i - 1][j + 1], max_l2[i][j - 1], max_l2[i][j + 1], max_l2[i + 1][j - 1], max_l2[i + 1][j], max_l2[i + 1][j + 1]] ) ) :
                        count += 1

print(count, file = file_output)