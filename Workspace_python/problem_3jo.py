# 1. 반지름 5 높이 7인 원기둥의 부피
import math
r = 5
h = 7
vol = math.pi * r * r * h
print(f'반지름이 {r}이고 높이가 {h}인 원기둥의 부피 : {round(vol,2)}')

# 2. 리스트를 정렬하고 역순으로 나열하세요.
a = [34, 36, 232, 40, 22, 113, 44, 74, 23, 2, 525, 25, 38]
print(sorted(a, reverse=True))

# 3. 오늘 날짜를 출력하고 3개월 뒤 일자를 출력하세요. 단, 한 달은 4주로 간주한다.
from datetime import date, datetime, timedelta
today = datetime.today().date()
aft3m_today = today + timedelta(weeks=12)
print(f'오늘 날짜 : {today} \t 3개월 뒤 날짜 : {aft3m_today}')

# 4. 변수(name)에 이름으로 문자열을 넣어서 hello, I'm {name}을 완성하자.
name = 'dongchan'
print(f'hello, I\'m {name}')

# 5. 8!를 계산하시오.
value = 1
for i in range(8,0,-1):
    value *= i
print(f'8! : {value}')

# 6. 방탄소년단 정국의 Dreamers 가사 중 d로 시작해서 s로 끝나는데,
#    사이에 적어도 문자가 한개 이상을 출력하시오!
import re
txt = "Ala Ho La Dan Ala Ho La Dan (Oh, Redone) Ala Ho La Dan Ala Ho La Dan Look Who We Are, We Are The Dreamers We Make It Happen, ’cause We Believe It Look Who We Are, We Are The Dreamers We Make It Happen ’cause We Can See It"
print(re.findall(r'd[a-zA-Z]+s]', txt))

# 7. 1에서 1000까지의 수를 랜덤으로 출력하세요.
import random
print(random.randint(1,1001))

# 8. 임의의 정수 5개를 리스트 형태로 출력하세요.
int5 = []
for i in range(5):
    int5.append(random.randint(-10000,10000))
print(int5)

# 9. number = ['8', '5', ' ', 'good', 'no'] 중 문자만 list로 출력하세요.
number = ['8', '5', ' ', 'good', 'no']
print(list(filter(lambda x : re.findall(r'[a-zA-Z]+', x), number)))

# 10. if 조건문을 이용해서 연령대를 구분하세요.
# 단, 연령대는 청년(20~39세), 중년(40~50세), 장년(51~65세)로 구분할 것.
# 벗어나는 숫자를 입력할 경우 '20~65 사이의 값을 입력해주세요!' 출력할 것.
# (최종 입력 나이: 30을 넣어 연령대를 확인하세요.)
age = int(input('나이를 입력하세요 : '))
if age >= 51 :
    print('장년')
elif age >= 40 :
    print('중년')
elif age >= 20 :
    print('청년')
else :
    print('20~65 사이의 값을 입력해주세요!')

# 11. 리스트 n,m을 합쳐서 [(1, 7), (3, 9), (5, 0), (6, 8), (4, 9)]로 만들자. 단 변수 m 을 수정 시 함수를 사용해야한다.
n = [1, 3, 5, 6, 4]
m = [7, 9, 0]
m.append(8)
m.append(9)
tuple_list = []
for i in range(len(n)):
    tuple_list.append((n[i],m[i]))
print(tuple_list)
# 12. 국어, 수학, 영어 성적을 입력받고, 평균이 90 점 이상이면 “A”,
# 평균이 80 점 이상이면 “B”,
# 평균이 70 점 이상이면 ”C",
# 나머지는 “D” 가 나오도록 프로그램하세요.
# TIP: if, elif, else 를 사용하시오.
kor, math, eng = map(int, input('국어점수, 수학점수, 영어점수 :').split(','))
avg = (kor + math + eng) / 3
if avg >= 90 :
    print('A')
elif avg >= 80 :
    print('B')
elif avg >= 70 :
    print('C')
else :
    print('D')