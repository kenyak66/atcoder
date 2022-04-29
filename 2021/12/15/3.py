n = int(input())

if n < 10:
    print(n)

else:
    a = n//9
    b = n%9

    if b != 0:
        print(str(b)*(a+1))
    else:
        print('9'*a)