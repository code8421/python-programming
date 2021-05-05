import random


# 랜덤한 숫자 세 자리를 만드는 함수
def rand():
    # 1. 0으로 채워진 세 칸짜리 random_numbers 리스트 생성
    random_numbers = [0, 0, 0]

    # 2. 0,1,2번째 인덱스의 값을 0부터 9까지 임의로 삽입
    random_numbers[0] = random.randrange(1, 10)
    random_numbers[1] = random.randrange(1, 10)
    random_numbers[2] = random.randrange(1, 10)

    # 3. 0번째 인덱스와 1번째 인덱스가 다를 때 까지 1번째 인덱스의 값을 다시 설정
    while random_numbers[0] == random_numbers[1]:
        random_numbers[1] = random.randrange(1, 10)

    # 4. 0번째 인덱스와 2번째 인덱스 혹은 1번째 인덱스와 2번째 인덱스의 값이 다를 때 까지
    #    2번째 인덱스의 값을 다시 설정
    while random_numbers[0] == random_numbers[2] or random_numbers[1] == random_numbers[2]:
        random_numbers[2] = random.randrange(1, 10)

    # 5. 만들어진 random_number 리스트를 리턴
    return random_numbers


# 야구 게임을 하는 함수 생성
def baseball(random_numbers):
    strike, ball, cnt = 0, 0, 0

    while True:
        user_num = input()
        for i in range(3):
            for j in range(3):
                if random_numbers[i] == int(user_num[j]) and i == j:
                    strike += 1
                elif random_numbers[i] == int(user_num[j]):
                    ball += 1

        print("스트라이크:", strike)
        print("볼:", ball)
        cnt += 1

        if strike == 3:
            break
        else:
            strike = 0
            ball = 0

    print(f"{cnt}번 만에 맞췄습니다!")


def main():
    with open('text.txt', encoding='utf-8') as f:
        for line in f:
            print(line)
    random_numbers = rand()
    baseball(random_numbers)


if __name__ == "__main__":
    main()
