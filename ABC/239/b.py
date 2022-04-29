# x = int(input())
# if x >= 10 | x % 10 == 0:
#     print(str(x)[0:len(str(x))-1])
# elif x >= 0:
#     print(0)
# elif x > -10:
#     print(-1)
# else:
#     print((str(x)[0:len(str(x))-1] - 1))
x = input()

y = 0
if x[0] == '-':
    
    y = int(x)
    if  x > 9:
        print(int(x[0:len(x)-1]))
    else:
        print(-1)

else:
    y = int(x)
    if y >= 10:
        print(x[0:len(x)-1])
    elif x >= 0:
        print(0)