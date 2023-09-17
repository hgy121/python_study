print('='*50)
nowY = int(input('현재년은?'))
nowM = int(input('현재월은?'))
nowD = int(input('현재일은?'))

birthY = int(input('출생년은?'))
birthM = int(input('출생월은?'))
birthD = int(input('출생일은?'))

if birthM<nowM:
    age = nowY - birthY
elif birthM==nowM:
    if birthD<nowD:
        age = nowY - birthY
    else:
        age = nowY - birthY - 1
else:
    age = nowY - birthY - 1

print('='*50)
print('오늘날짜 : %d년 %d월 %d일'%(nowY,nowM,nowD))
print('생년월일 : %d년 %d월 %d일'%(birthY,birthM,birthD))
print('-'*50)
print('만 나이 : %d세'%age)
print('='*50)