list01 = list()
for i in range(1,11) :
    list01.append(i)
print(list01)

# 한 줄로 표현
list02 = [i for i in range(1,11)]
print(list02)

# 1 ~ 10 사이의 짝수만 if 기준 왼쪽은 True 오른쪽은 False
list03 = [i for i in range(1,11) if i % 2 == 0]
print(list03)
# 다음과 동일.
# for i in range(1,11) :
#     if i % 2 == 0 :
#         list03.append(i)

# a를 포함한 데이터들을 새로운 리스트로 만들고 싶다.
subjects = ['python', 'analysis', 'database', 'html', 'css',
            'javascript', 'django', 'science', 'engineering']

list04 = [subject for subject in subjects if 'a' in subject]
print(list04)

# 다음과 동일
# list04 = list()
# for subject in subjects :
#     if 'a' in subject :
#         list04.append(subject)
# print(list04)

# 중첩
# [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15]]
list05 = [[4*i + j for j in range(4)] for i in range(4)]
print(list05)

# 다음과 동일
# list05 = list()
# for i in range(4) :
#     list05.append(list())
#     for j in range(4) :
#         list05[i].append(4 * i + j)
# print(list05)
