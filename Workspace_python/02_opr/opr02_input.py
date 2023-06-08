# a = input()
# print(a)
# print(type(a))
# input 으로 입력받은 값은 모두 문자열이다.

# name = input("이름을 입력하세요 : ")
# print(f'입력된 이름은 {name} 입니다.')

# 이름, 국어점수, 영어점수, 수학점수를 입력받아서
# {'name': ??, 'kor': ??, 'eng': ??, 'math': ??, 'sum' : ??, 'avg': ??}
# 라는 형태로 출력하자.
# sum : 점수의 총합 / avg : 점수 평균
# name, kor, eng, math = input().split()
# kor, eng, math = map(int, list(kor,eng,math))
# sum = kor + eng + math
# avg = sum / 3
# print(f'name : {name}, kor : {kor}, eng : {eng}, math : {math}, sum : {sum}, avg : {avg}')

name = input("이름 입력 : ")
kor = input("국어 점수 : ")
eng = input("영어 점수 : ")
math = input("수학 점수 : ")
sum = int(kor) + int(eng) + int(math)
avg = sum / 3

score = dict()

score['name'] = name
score['kor'] = kor
score['eng'] = eng
score['math'] = math
score['sum'] = sum
score['avg'] = avg

print(score)

# <중> 영수증 만들기 - 물건, 가격, 수량 입력 -> if '끝' -> 합계 나오는 문제
#
# 코딩까지도
# <상> 가위바위보 - 1:가위 2:바위 3:보 이하 -> 장연진 너무 어렵게 내실까봐...
# <하> 혜린 <>