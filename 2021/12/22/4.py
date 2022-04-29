a, b, c = map(int, input().split())

if c%2 == 0:
    if abs(a*c) > abs(b*c):
        print(">")
    if abs(a*c) < abs(b*c):
        print("<")
    if abs(a*c) == abs(b*c):
        print("=")

else:
    if a*c > b*c:
        print(">")
    if a*c < b*c:
        print("<")
    if a*c == b*c:
        print("=")