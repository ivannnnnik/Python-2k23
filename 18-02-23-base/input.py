a = int(input())
if (a // 10000 == 0) and (a // 1000 != 0)  and (a % 7 == 0 or a % 17 == 0):
    print('YES')
else:
    print('NO')