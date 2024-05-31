numbers = [19, 13, 2, 5, 3, 11, 7, 12]

new_list = sorted(numbers) #작은 숫자대로 정렬
print(new_list)

new_list= sorted(numbers, reverse=True) #큰 숫자대로 정렬
print(new_list)

print(numbers.sort()) #아무것도 리턴 X
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#sorted 기존 리스트 건들이지 않음. 정렬된 새로운 리스트를 라턴
#sort 아무것도 리턴하지 않고, 기존 리스트를 정렬



#reverse
numbers = [5, 3, 7, 1] 
numbers.reverse() #원소들을 뒤집어진 순서로 배치합니다.
print(numbers)

#index
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수")) #원소의 인덱스를 리턴해줍니다.
print(members.index("태호"))

#remove
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플") #"~~~"값을 갖고 있는 원소를 삭제해줍니다.
print(fruits)
