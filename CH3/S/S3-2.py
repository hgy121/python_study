hour1 = int(input('첫 번째 시간의 시를 입력하세요 : '))
min1 = int(input('첫 번째 시간의 분를 입력하세요 : '))
hour2 = int(input('두 번째 시간의 시를 입력하세요 : '))
min2 = int(input('두 번째 시간의 분를 입력하세요 : '))

if hour1==hour2:
    fastH = hour2 
    slowH = hour1
    if min1<min2:
        fastM = min1
        slowM = min2
    else : 
        fastM = min2
        slowM = min1
elif hour1<hour2:
    fastH = hour1
    slowH = hour2
    fastM = min1
    slowM = min2
else:
    fastH = hour2
    slowH = hour1
    fastM = min2
    slowM = min1

print('-빠른 시간 : %d:%d'%(fastH,fastM))
print('-늦은 시간 : %d:%d'%(slowH,slowM))
