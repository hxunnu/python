b#key-value pair (키-값 쌍)
my_dictionart = {
  5: 25,
  2: 4,
  3: 9
}

print(my_dictionart[3])

my_dictionart[9] = 81 #사전에 키, 값을 추가하는 방법

print(my_dictionart) 

#리스트의 인덱스는 0, 1, 2, 3 정숫값으로 차례대로지만 사전은 정수 X, 순서대로 X

my_family = {
  '엄마': '혜',
  '아빠': '영',
  '딸': '주',
  '아들': '현'
}

print(my_family)
print(my_family['아들'])

print('혜' in my_family.values()) #'혜'라는 값이 my_family 사전에 있는지 확인 하는 문구

for value in my_family.values():
  print(value)

print(my_family.keys())

for key in my_family.keys():
  value = my_family[key]
  print(key, value)

for key, value in my_family.items():
  print(key, ':', value)