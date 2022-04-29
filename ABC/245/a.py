a, b, c, d = map(int, input().split())

t = a*60*60 + b*60
a = c*60*60 + d*60 + 1
# print(t, a)
print('Takahashi' if t<a else 'Aoki')