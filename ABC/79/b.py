def main():
    n = int(input())

    l = [0]*(n+1)
    l[0] = 2

    for i in range(1, n+1):
        if i == 1:
            l[i] = 1
        else:
            l[i] = l[i-1] + l[i-2]
    print(l[n])

main()