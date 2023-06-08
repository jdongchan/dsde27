
# 3 영수증 문제
# market이 있다. market의 물건을 여러 번 입력하다가 '끝'을 입력하면
# 합계금액을 출력하는 while문을 작성하여라.
market = {'오징어' : 2000, '사과' : 2000, '감자' : 1500}
sum = 0
while True:
    good = input()
    if good == '끝':
        print(f'합계금액은 {sum}입니다.')
        break
    price = market.get(good)
    sum = sum + price


# 4 태어난 연도를 입력받아,
# 1964년 전에 태어났다면, '베이비부머'
# 1980년 전에 태어났다면, 'X세대'
# 1996년 전에 태어났다면, '밀레니얼'
# 1996년 이후에 태어났다면, 'Z세대' 를 출력하는 if문을 만들어주세요.
y = int( input( '언제 태어났나요?' ) )

gen = None

if y <= 1964:
    gen = '베이비부머'
elif y <= 1980:
    gen = 'X세대'
elif y <= 1996:
    gen = '밀레니얼'
else:
    gen = 'Z세대'

print(f"당신은 {gen}입니다.")

# 5. 사용자에게 가격과 할인율(두자리 숫자)을 입력받아 할인된 금액을 print하는 명령문을 작성하여라.

amt = int(input())
discount_rate = int(input())
amt_discounted = int(amt * (1 - 0.01 * discount_rate))
print(amt_discounted)