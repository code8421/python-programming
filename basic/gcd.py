# 두 정수의 최대공약수(Greatest Common Divisor) 계산하는 함수
def get_gcd(a, b):
    while b != 0:
        result = b
        a, b = b, a % b
    
    return result


def test_get_gcd():
    assert(get_gcd(21, 12) == 3)
    print("테스트 통과!")


if __name__ == '__main__':
    test_get_gcd()
