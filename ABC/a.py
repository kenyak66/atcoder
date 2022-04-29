a, b, c, d, e, f, x = map(int, input().split())

T = (x//(a+c) * a + min((x%(a+c)), a)) * b
A = (x//(d+f) * d + min((x%(d+f)), d)) * e
if T > A:
    print('Takahashi')
elif A > T:
    print('Aoki')
else:
    print('Draw')