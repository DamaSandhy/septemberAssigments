y = int(input())
d = y % 400 == 0
d_4_and_100 = (y % 4 == 0) and (y % 100 != 0)
if d or d_4_and_100:
    print("True")
else:
    print("False")
