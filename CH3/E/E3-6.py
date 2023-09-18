a = int(input('수를 입력하세요 : '))

if a<10:
    print('%d은(는) 한 자리 숫자이다.'%a)
elif a<100:
    print('%d은(는) 두 자리 숫자이다.'%a)
elif a<1000:
    print('%d은(는) 세 자리 숫자이다.'%a)
else: 
    print('오류! %d은(는) 범위(0~999) 이외의 숫자이다.'%a)