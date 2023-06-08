def coffee(quantity, price):
    change = price - (quantity * 100)

    if change >= 0 :
        prn(quantity, change)
    else :
        prn()

def prn(quantity = 0, change = 0):
    if quantity == 0 and change == 0:
        print('금액이 부족합니다.')
    else:
        print(f'커피 {quantity}잔이 나왔습니다. 잔돈은 {change}원 입니다.')

def start():
    q = int(input('커피 몇 잔이 필요하신가요? :'))
    p = int(input('금액을 넣어주세요 (커피 한 잔에 100원) : '))
    coffee(q, p)

