with open('vocabulary.txt', 'a', encoding="utf-8") as f:
  vocab_eng = ""
  vocab_kor = ""
  while True:
    vocab_eng = input("영어 단어를 입력하세요 : ")
    if vocab_eng == "q":
      break
    vocab_kor = input("한국어 뜻을 입력하세요 : ")
    if vocab_kor == "q":
      break
    f.write(f"{vocab_eng}: {vocab_kor}\n")