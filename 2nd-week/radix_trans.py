# Lab 2-1

def radix_trans_in(n, m, r=2):
    # 더 이상 나눌 숫자가 없을 때까지 나눈다.
    if n == 0:
        return
    else:
        radix_trans_in(n // r, m, r)
    # 나머지 연산 결과를 나눗셈 순서의 역순으로 출력한다.
    # 나머지 연산 결과를 진법별 숫자 기호에 대입한다.
    print(m[r][n % r], end='')

# 지원하는 진법: 2진법, 8진법, 16진법
def radix_trans(n, r=2):
    m = dict()
    m[2] = "01"
    m[8] = "01234567"
    m[16] = "0123456789ABCDEF"
    radix_trans_in(n, m, r)
    print()

X=202500062
radix_trans(X, 2)
radix_trans(X, 8)
radix_trans(X, 16)
