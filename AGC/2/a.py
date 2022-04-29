a, b = map(int, input().split())
if a <= 0 | 0 <= b:
    print('Zero')
elif 0 < a:
    print('Positive')
elif b < 0 | (b-a) % 2 == 1:
    # print(b-a, (b-a) % 2)
    print('Positive')
else:
    # print(b-a, (b-a) % 2)
    print('Negative')