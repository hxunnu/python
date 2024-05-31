'''
구구단 프로그램을 while문이 아닌 for문을 사용해서 만들어 보세요.
실습 결과




1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
.
.
.
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
'''

#방법 1 파리미터 1개 사용

for i in range(9):
    for j in range(9):
        print(f"{i+1} * {j+1} = {(i+1) * (j+1)}")

#방법 2 파라미터 2개 사용

for i in range(1, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i*j))


for a in range(1, 400):
    for b in range(1, 400):
        for c in range(1, 400):
            if a * a + b * b == c * c and a < b < c and a + b + c == 400:
                print(a * b * c)