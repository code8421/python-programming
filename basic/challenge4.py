birthday = input("생년월일 6자리로 입력해주세요. (yymmdd): ")
y = birthday[:2]
m = birthday[2:4]
d = birthday[4:]
print(f"당신의 생일은 {y}년 {m}월 {d}일입니다.")
