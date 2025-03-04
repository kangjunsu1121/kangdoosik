from random import *
a = list(range(1,51))
c = 0
for i in a :
    b = randrange(5,51)
    if b <= 15 :
        print(f'[o] {i}번째 손님 (소요시간 : {b}분)')
        c += 1
    else :
        print(f'[] {i}번째 손님 (소요시간 : {b}분)')
print(f'총 탑승 승객 : {c} 분')

