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

'''
'피타고라스 정리'라고 들어 보셨나요? 직각삼각형에서, 빗변의 제곱이 두 직각변의 제곱의 합과 같다는 정리입니다.

거기서 나온 '피타고라스 삼조'라는 개념이 있는데요. 피타고라스 삼조란, 피타고라스 정리(﻿a2+b2=c2a2+b2=c2)를 만족하는 세 자연수 쌍 ﻿(a,b,ca,b,c)﻿입니다.

예를 들어, ﻿32+42=5232+42=52이기 때문에 ﻿(3,4,53,4,5)는 피타고라스 삼조입니다.

a<b<ca<b<c라고 가정할 때, a+b+c=400a+b+c=400을 만족하는 피타고라스 삼조(a,b,ca,b,c)﻿는 단 하나인데요. 이 경우, a∗b∗ca∗b∗c는 얼마인가요?
'''

for a in range(1, 400):
    for b in range(1, 400):
        for c in range(1, 400):
            if a * a + b * b == c * c and a < b < c and a + b + c == 400:
                print(a * b * c)
