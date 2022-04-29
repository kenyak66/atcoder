x1, y1, x2, y2 = map(int, input().split())
ans = []

z1 = y1 - (y2 - x2)
z2 = y2 + (y1 - x1)
w1 = x1 - (y2 - x2)
w2 = x2 + (y1 - x1)

ans.append(z1)
ans.append(z2)
ans.append(w1)
ans.append(w1)
print(*ans)