print("순서대로 별찍기")
for i in range(1, 11):
    print('*' * i)

print("\n2단위로 별찍기")
for i in range(1, 11, 2):
    print('*' * i)

print("\n거꾸로 별찍기 (1)")
for i in range(1, 11):
    print('*' * (11-i))

print("\n거꾸로 별찍기 (2)")
for i in range(10, 0, -1):
    print('*' * i)
