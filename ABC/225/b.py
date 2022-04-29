n = int(input())
l = [list(map(int, input().split())) for _ in range(n - 1)]
 
def star(x):
    flg = True
 
    for i in range(1, n - 1):
        if (l[i][0] != x) & (l[i][1] != x):
            flg = False
            break
        
    return flg
 
if star(l[0][0]) | star(l[0][1]):
    print("Yes")
else:
    print("No")