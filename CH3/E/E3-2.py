a = int(input('첫 번째 수를 입력하세요 : '))
b = int(input('두 번째 수를 입력하세요 : '))
if a>b:
    s = '보다 크다.'
elif a<b:
    s = '보다 작다.'
else:
    s = '와(과) 같다.'

print('%d은(는) %d %s'%(a,b,s))