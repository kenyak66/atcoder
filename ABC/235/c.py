n, q = map(int, input().split())
a = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(q)]

#print(a)

for i in range(q):
    #print(a.count(query[i][0]), query[i][1])
    if a.count(query[i][0]) >= query[i][1]:
        cnt = 0
        for j in range(n):
            if a[j] == query[i][0]:
                cnt += 1
                if cnt == query[i][1]:
                    print(j+1)

    else:
        print(-1)
        continue