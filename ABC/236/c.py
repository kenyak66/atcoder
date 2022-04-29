n = int(input())

inf = 998244353
num = len(str(n))
ans = 0

a = ((10**(num-1))*((10**(num-1) - 1)))/2
b = (9 * (10**(num - 1)) - 9)/(10 - 1)
c = 10**(num - 1) - 1
ans += a - b + c
print(ans)
A = (n - 10**(num - 1) + 1)*(10**(num - 1) + n)/2
B = 10**(num - 1) * (n - 10**(num - 1) + 1)
C = (n - 10**(num - 1) + 1)
ans += A - B + C
print(int(ans%inf))