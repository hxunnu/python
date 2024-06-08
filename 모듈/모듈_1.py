import datetime

pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(type(pi_day))

today = datetime.datetime.now()
print(today)
print(type(today))

today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day))

today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)

print(today)
print(today + my_timedelta)

today = datetime.datetime.now()

print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초

today = datetime.datetime.now()

print(today)
print(today.strftime("%b, %B %dth %Y"))

import random

random_number = random.randint(1, 20)

chance = 4

while chance != 0:
        geuss_random_number = int(input(f"기회가 {chance}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
        if random_number < geuss_random_number:
            print("Down")
        elif random_number > geuss_random_number: 
            print("UP")
        elif random_number == geuss_random_number:
            print(f"축하합니다. {4-chance}번만에 숫자를 맞히셨습니다.")
            break
        chance -= 1

if chance == 0 :
  print(f"아쉽습니다. 정답은 {random_number}였습니다.")
