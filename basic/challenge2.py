data = ["조회수: 1,500", "조회수: 1,002", "조회수: 300", "조회수: 251",
        "조회수: 13,432", "조회수: 998"]
sum = 0

for i in data:
    n = int(i.split(' ')[1].replace(',', ''))
    sum += n
    print(n)

print(f'총 합: {sum}')
