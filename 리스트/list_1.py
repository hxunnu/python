numbers = [2, 3, 5, 7, 11, 13]
names = ["현준", "우철", "재윤", "동훈"]

#인덱싱 
print(numbers[1])
print(names[0])

print(numbers[3] + numbers[5])

print(numbers[-3]) # [0, 1, 2, 3, 4, 5] 이런식으로 번호가 매겨짐. 또한, [-6, -5, -4, -3, -2, -1] 로도 가능함 

#리스트 슬라이싱

print(numbers[0:4]) # 0~4번째의 리스트 항목을 보여달라

new_list = numbers[2:] #number에 들어가있는 항목중 2번째 이후의 항목을 new_list로 넘겨라
print(new_list[3]) #2번째 이후의 항목을 정리한 리스트중애서 3번쨰 항목애 있는 값을 띄워라


numbers =[]

numbers.append(3) 
numbers.append(7) #추가 연산

print(numbers)
print(len(numbers)) #list의 갯수

numbers = [2, 3, 5, 7, 9, 11, 13, 14]
del numbers[3]
print(numbers)
numbers.insert(4, 33)
print(numbers) #삽입 연산