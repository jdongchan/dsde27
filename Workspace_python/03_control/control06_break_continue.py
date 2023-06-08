# break : 반복문 종료 후 다음 명령 수행
i = 1
while i <= 10 :
    if i > 5 :
        break
    print(i, end=' ')
    i +=1
print()

# continue : 아래의 명령들을 무시하고 다음 반복으로 진행
for i in range(10):
    if i % 2 == 0 :
        continue
    print(i, end=' ')
print()

for i in range(3, 0, -1) :
    print(i, end=' ')
else :
    print('go!')
# else 비교
for i in range(10) :
    if i % 2 != 0 :
        continue
        # 다음 반복으로 넘어가시오.
    print(i, end= ' ')
# 끝까지 반복이 종료되었을 때 else 구문 실행
else :
    print('짝수 출력?')

for i in range(10) :
    if i > 5:
        break
        # 만나서 반복이 중간에 종료되었음.
    print(i, end= ' ')
# 끝까지 반복이 되지 않았기 때문에 else 구문 실행 안됨.
else :
    print('5까지 출력?')

