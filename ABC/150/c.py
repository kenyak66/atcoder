import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

per = list(itertools.permutations(range(1, n+1), n))
print(abs(per.index(p)  - per.index(q)))