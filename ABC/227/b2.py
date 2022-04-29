def f(x):
	return x * (x * (x + 1) + 2) + 3

n = float(input())

left = 0
right = 100

while (right - left > 1e-1):
	mid = (right + left)/2
	if (f(mid) < n):
		left = mid
	else:
		right = mid
    #print(left, right)
#print(right)
print(left)