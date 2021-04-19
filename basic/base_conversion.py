# 다른 진법의 숫자(2 ~ 10)를 10진수로 변환하는 함수
def convert_to_decimal(number, base):
    multiplier, result = 1, 0

    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number //= 10
    
    return result


# 10진수를 다른 진법의 숫자로 변환하는 함수
def convert_from_decimal(number, base):
    strings = "0123456789ABCDEF"
    result = ""

    while number > 0:
        digit = number % base
        result = strings[digit] + result
        number //= base
    
    return result


# 재귀(Recursive)함수를 사용한 진법 변환
def recursive_func(number, base):
    strings = "0123456789ABCDEF"

    if number < base:
        return strings[number]
    else:
        return recursive_func(number // base, base) \
            + strings[number % base]


def test_func():
    assert(convert_to_decimal(1001, 2) == 9)
    assert(convert_from_decimal(31, 16) == "1F")
    assert(recursive_func(9, 2) == "1001")
    print("테스트 통과!")


if __name__ == "__main__":
    test_func()
