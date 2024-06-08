import random
vocab = {}
with open('file\ocab.txt', 'r', encoding="utf-8") as f:
    for line in f:
        data = line.strip().split(": ")
        eng_word = data[0] # 정답
        kor_word = data[1] #질문 
        vocab[eng_word] = kor_word


keys = list(vocab.keys())  

while True:
  index = random.randint(0, len(keys) - 1)
  eng_word = keys[index]
  kor_word = vocab[eng_word]

  sol = input(f"{kor_word}: ")

  if sol == 'q':
        break

  if sol == eng_word:
    print("맞았습니다!")
  else:
    print(f"아쉽습니다. 정답은 {eng_word}입니다.")
            