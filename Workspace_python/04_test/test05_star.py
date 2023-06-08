'''
*
**
***
****
*****
'''
def star01():
    for i in range(5):
        print('*' * (i+1))
    print('----------')


'''
*****
****
***
**
*
'''
def star02():
    for i in range(5):
        print('*' * (5-i))
print('----------')

'''
    *
   **
  ***
 ****
*****
'''

print('----------')
def star03():
    for i in range(5):
        print(' ' * (4-i) + '*' * (i+1))




'''
*****
 ****
  ***
   **
    *
'''
def star04():
    pass




'''
    *
   ***
  *****
 *******
*********
'''
def star05():
    pass


if __name__ == '__main__':
    star01()
    star02()
    star03()
    star04()
    star05()
