n = int(input())
t = input()

x = 0
y = 0

dir = 0

for i in t:
    if i == 'S':
        if dir%4 == 0:
            x += 1
        if dir%4 == 1:
            y -= 1
        if dir%4 == 2:
            x -= 1
        if dir%4 == 3:
            y += 1
    else:
        dir += 1

print(x, y)