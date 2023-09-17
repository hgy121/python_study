a = int(input('첫 번째 수를 입력하세요 : '))
b = int(input('두 번째 수를 입력하세요 : '))
c = a+b
if b%3==0:
    s = '이다.'
else:
    s = '가 아니다.'
print('%d + %d = %d\n%d은(는) 3의 배수%s'%(a,b,c,c,s))