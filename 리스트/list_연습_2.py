'''
습 설명

화씨 온도(°F)를 섭씨 온도(°C)로 바꾸어주는 프로그램을 만들려고 합니다.


화씨 온도를 섭씨 온도로 변환해 주는 함수 fahrenheit_to_celsius를 써 보세요. 이 함수는 파라미터로 화씨 온도 fahrenheit를 받고, 변환된 섭씨 온도를 리턴합니다.
'''

def f_t_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 1)

# 화씨 온도 리스트
f = [40, 15, 32, 64, -4, 11]

# 섭씨 온도 리스트
c = []


i = 0

while i < len(f): #화씨 온도 리스트의 항목의 개수만큼 while문 작동
    c_1 = f_t_c(f[i]) #섭씨를 저장할 변수에 f_t_c함수를 부르는데 호출값은 화씨 온도리스트에서 i번째 값을 반환해 저장
    c.append(c_1) #섭씨 온도 리스트에 차래대로 c_1값을 넣어줌
    i += 1 #i에 1을 더함

# 결과 출력
print("화씨 온도 리스트:", f)
print("섭씨 온도 리스트:", c)
