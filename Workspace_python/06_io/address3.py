'''
address.txt 파일에
이름, 010-0000-0000, 경기도 00시 ...
저장해주세요.
만일, address.txt 파일이 없으면 새로 만들어서 저장
있으면 아래줄에 추가해주세요.
++ bonus option ++
menu
1 : 전체출력
2 : 이름으로 검색
3 : 주소록 입력
4 : 종료
'''

def address_input():
    with open('address.txt','a') as file:
        name, phone, address = input('이름, 전화번호, 주소를 입력해주세요 : ').split(',')
        file.write(name+',')
        file.write(phone+',')
        file.write(address+'\n')

'''
address.txt 파일에서
((한 줄씩)) 읽어와서
파일 전체를 출력해주세요.
'''

def address_print():
    with open('address.txt', 'r') as file:
        for line in file.readlines():
            print(line)

def address_search():
    with open('address.txt', 'r') as file:
        search_name = input('검색할 이름을 입력해주세요 : ')
        for line in file.readlines():
            if search_name in line:
                print(line)
        # 검색결과가 없는 경우도 구현하고 싶은데 잘 모르겠습니다.

if __name__ == '__main__':
    while True:
        menu = '''
        *****
        1 : 전체 출력
        2 : 이름으로 검색
        3 : 주소록 입력 (이름, 전화번호, 주소)
        4 : 프로그램 종료
        '''
        print(menu)
        select = int(input('입력해주세요 : '))

        match select:
            case 1:
                address_print()
            case 2:
                address_search()
            case 3:
                address_input()
            case 4:
                break
            case _:
                print('다시 입력해 주세요...')
    print('주소록을 종료합니다...')