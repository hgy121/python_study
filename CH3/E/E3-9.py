a = int(input('점수를 입력하세요 : '))

if a<=100 and a>=90:
    print('-성적:%d, 등급:수'%a)
elif a<=89 and a>=80:
    print('-성적:%d, 등급:우'%a)
elif a<=79 and a>=70:
    print('-성적:%d, 등급:미'%a)
elif a<=69 and a>=60:
    print('-성적:%d, 등급:양'%a)
elif a<=59 and a>=0:
    print('-성적:%d, 등급:가'%a)
else :
    print('입력 오류!')