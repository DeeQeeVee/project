file_input = open("TONG.inp", "r")
file_output = open("TONG.out", "w")

n, p, k = map(int, file_input.readline().split())

a = list(map(int, file_input.read().split()))
sum = 0

for i in a:
        sum += i

l, t, count, x, ans = 0, 0, 0, 0, 0
m = 1000000007

l = k - (n * (k / n))
if (l == 0):
        l = n

for i in range(l - 1, n):
        if (count == p):
                break

        t += a[i]
        count += 1

if (count == p):
        print(t % m, file = file_output)

else:
        p = p - count
        x = p / n
        p = p - (n * x)

        for i in range(0, int(p)):
                t = t + a[i]

        sum = ((sum % m) * (x % m)) % m
        t = t % m

        ans = (sum + t) % m
        print(ans, file = file_output)