char = ["티모", "리신", "이즈리얼"]

for name in char:
  if name == "티모":
    print("좆모")
  elif name == "리신":
    print("어디로 가야하오?")
  elif name == "이즈리얼":
    print("어쩔")

  #range

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  print(i)

for i in range(3, 11): #3 ~ 10까지를 출력 range(start, stop) 이라면 start로 시작해서 stop-1로 끝남
  print(i)
  
for i in range(10): #0에서 부터 9까지 출력 range(stop) 이라면 0 ~ stop-1까지의 범위 
  print(i)

for i in range(3, 17, 3): #3에서 부터 16까지 3증가하면서 출력 range(start, stop, step) 이라면 start부터 stop-1까지의 범위에서 step씩 증가
  print(i)

#range 함수 장점 : 간편함, 깔끔함, 메모리 효율성