h, w = map(int, input().split())

ans = 0
if (h==1) | (w==1):
    ans = 1
elif h%2 == 0:
    ans = (h//2) * w
elif w%2 == 0:
    ans = (w//2) * h
else:
    ans = ((h//2)+1) * ((w//2)+1) + (h//2) * (w//2)

print(ans)