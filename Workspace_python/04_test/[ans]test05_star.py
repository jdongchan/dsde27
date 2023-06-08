'''
*
**
***
****
*****
'''

def star01():
    for i in range(1,6):
        print('*' * i)
    print('-----------')

'''
*****
****
***
**
*
'''

def star02():
    for i in range(5,0,-1):
        print('*' * i)
    print('-----------')

'''
    *
   **
  ***
 ****
*****
'''
def star03():
    for i in range(1,6):
        print(' '*(5-i) + '*' * i)
    print('----------')
'''
*****
 ****
  ***
   **
    *
'''
def star04():
    for i in range(5):
        print(' ' * i + '*' * (5 - i))
    print('----------')

'''
    *
   ***
  *****
 *******
*********
'''
def star05():
    for i in range(5):
        print(' '* (4 - i) + '*' * (2 * i + 1))


if __name__ == '__main__':
    star01()
    star02()
    star03()
    star04()
    star05()
