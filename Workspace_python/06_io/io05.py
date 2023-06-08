file = open('test01.txt', 'r', encoding = 'utf-8')
read_txt = file.read() # 여기서 이미 파일을 다 읽었기 때문에
print(read_txt)

readline_txt = file.readline() # 여기서는 이제 읽을 게 없다.
print(readline_txt)

readlines_txt = file.readlines()
print(readlines_txt)

file.close()

# 즉 커서가 지나가는 개념으로 이해하면 쉬울 듯.