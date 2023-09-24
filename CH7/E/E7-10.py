def cm(c):
    inch = c*0.393701
    return inch
def kg(c):
    pound = c*2.204623
    return pound


print('-선택 옵션')
print('1.길이 환산(센티미터 --> 인치)\n2.무게 환산(킬로그햄 --> 파운드)')
a = input('원하는 환산 단위를 선택하세요.(1/2): ')

if a == '1':
    c = int(input('센티미터 단위의 길이를 입력하세요 : '))
    print('%d센티미터 --> %.2f인치'%(c,cm(c)))
else :
    c = int(input('킬로그램 단위의 길이를 입력하세요 : '))
    print('%d킬로그램 --> %.2f파운드'%(c,kg(c)))

