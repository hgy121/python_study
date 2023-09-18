a = (input('숫자를 입력하세요 : '))
a = int(a[2] )
if a%2==0:
    s = '짝수'
else:
    s = '홀수'
print('%d은(는) %s이다.'%(a,s))