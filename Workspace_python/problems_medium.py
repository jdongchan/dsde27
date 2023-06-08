# 1. 영수증 만들기
# 물건 가격 수량을 입력하다가,
# 물건에 '끝'을 입력하면 실행이 멈추고 구매목록과 합계금액이 나오도록 하는 while문을 작성하여라.
sum = 0
item_list = []
while True:
    item = str(input())
    if item == '끝': # 이게 작동을 안하는 듯
        print(f'구매목록 : {item_list}')
        print(f'합계금액 : {sum}')
        break
    price = int(input())
    quantity = int(input())
    sum = sum + (price * quantity)
    item_list.append(item)
print()

# 2. 위의 영수증 구매목록에서 2글자 이상의 물건을 출력하시오.
print(list(filter(lambda x : len(x) >= 2, item_list)))
