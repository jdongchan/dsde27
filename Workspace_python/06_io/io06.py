with open('test01.txt', 'r', encoding = 'utf-8') as file:
    for line in file.readlines():
        print(line)

# with open 사용하면 자동으로 close
# io1 ~ io5 까지 with open으로 작성해볼 것.
