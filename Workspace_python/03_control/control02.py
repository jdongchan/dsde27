# 비어 있는 문자열은 False로 취급
if "" :
    print('False')
elif "안비었음" :
    print('True')
else :
    print('비어있으면 False로 취급')

# 비어있는 [], {}, () 또한 False로 취급
if [] :
    print('[] : False')
elif {} :
    print('{} : False')
elif () :
    print('() : False')
elif [1, 2] :
    print('True!')

# 0 : False/ 1 : True
if 0 :
    print(False)
elif 1 :
    print(True)

# None 타입도 False로 간주
if None :
    print('False')
else :
    print('True')

