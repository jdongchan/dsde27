import pickle

score = {'name': 'hong-gd', 'kor': 100, 'eng': 100, 'math': 100}

with open('test02.txt', 'wb') as file:
    pickle.dump(score, file)


'''
pickling 명령어 dump : 객체를 파일에 바로 저장한다.
unpickling 명령어 load : 파일에서 객체로 가지고 올 수 있다.
'''