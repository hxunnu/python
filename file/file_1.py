
with open('chicken.txt', 'r', encoding="utf-8") as f:
  for line in f:
    print(line.strip()) #stri[p]


with open('chicken.txt', 'r') as f:
    total_revenue = 0
    total_days = 0
    
    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])  # 그날의 매출
        
        total_revenue += revenue
        total_days += 1
        
    print(total_revenue / total_days)