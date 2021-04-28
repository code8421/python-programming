import random


def lottoMachine():
    lotto = []

    while len(lotto) < 6:
        num = random.randrange(1, 46)

        if num not in lotto:
            lotto.append(num)

    lotto.sort()

    return lotto


def main():
    for _ in range(5):
        print(lottoMachine())


if __name__ == "__main__":
    main()
