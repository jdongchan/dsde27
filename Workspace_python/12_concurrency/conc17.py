def people():
    result = list()
    while True:
        person = yield result # yield(send로 파라미터를 전달받음.)는 대기, 오른쪽에 있는 변수는 함수의 리턴 값
        result.append(person)

if __name__ == '__main__':
    co_people = people()
    next(co_people) # next는 이 제네레이터를 실행시켜준다.

    print(co_people.send('홍길동'))
    print(co_people.send('김선달'))
    print(co_people.send('이순신'))

# 1. 넥스트 호출
# 2. 제네레이터 1번 실행 (반복 한 번 거침)
# 3. 홍길동을 yield에 보냄
# 4. 홍길동 리스트에 어팬드
# 5. 와일로 반복
# 6. yield로 홍길동 리턴
# 7. 김선달 yield에 보냄
# 8. 김선달 어팬드
# 9. 와일 반복
# 10. yield로 김선달, 홍길동 리턴
