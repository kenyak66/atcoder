S1 = input()
S2 = input()
S3 = input()

l2 = []

l2.append(S1)
l2.append(S2)
l2.append(S3)

if l2.count("ABC") == 0:
    print("ABC")
elif l2.count("AGC") == 0:
    print("AGC")
elif l2.count("AHC") == 0:
    print("AHC")
elif l2.count("ARC") == 0:
    print("ARC")