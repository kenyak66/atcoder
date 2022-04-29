n = int(input())
a = list(map(int, input().split()))

ans = [360]
if n == 1:
    ans[0] -= a[0]
else:
    for i in range(n):
        sum = 0
        while(sum + ans[0] < a[i]):
            sum += ans[0]
            ans = ans[1:] + [ans[0]]
            # print(ans)

        # print(ans)
        ans.insert(0, ans[0]- (a[i] - sum))
        ans.insert(n, a[i] - sum)
        ans.remove(ans[1])
        # print(ans)
        # print("--------")

print(max(ans))