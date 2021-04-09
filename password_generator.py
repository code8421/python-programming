import random


print("비밀번호 생성기")

strings1 = "abcdefghijklmnopqrstuvwxyz"
strings2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
strings3 = "!@#$%^&*-_+,./"
strings4 = "0123456789"
strings = strings1 + strings2 + strings3 + strings4

pwd_num = int(input("생성할 비밀번호 갯수: "))
length = int(input("생성할 비밀번호 길이: "))

print("\n--- 비밀번호 생성 ---")

for pwd in range(pwd_num):
    password = ""
    for c in range(length):
        password += random.choice(strings)
    print(password)
