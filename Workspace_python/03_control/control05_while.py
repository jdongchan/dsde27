# while 조건 :
# 해당 조건이 True인 동안 반복

i = 1
while i <= 10 :
    print(i)
    i += 1

my_sum = 0
my_count = 1
while my_count <= 10 :
    my_sum += my_count
    my_count += 1
# while에서 else는 반복문이 정상적으로 수행됐을 때 출력
else :
    print(f'sum : {my_sum}\tcount : {my_count} ')

my_sum_02 = 0
for count in range(1,11) :
    my_sum_02 += count
    if count == 10 :
        my_count_02 = count
print(f'sum : {my_sum_02}\tcount : {my_count_02}')