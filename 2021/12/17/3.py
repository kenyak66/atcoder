l = list(map(int, input().split()))

ans = 1
inf = 998244353

for i in range(3):
    ans *= ((l[i] * (l[i] + 1))//2) % inf
    ans %= inf
    
print(int(ans))