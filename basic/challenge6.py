# 선수교체 프로그램 만들기

players = ['황의조', '황희찬', '구자철', '이재성', '기성용']

print('현재 경기 중인 선수')
for player in players:
    print(player)

print('-' * 40)

num_out = int(input('OUT 시킬 선수 번호: '))
del players[num_out]

name_in = input('IN 할 선수 이름: ')
players.append(name_in)

print('-' * 40)
print('교체 결과')

for player in players:
    print(player)
