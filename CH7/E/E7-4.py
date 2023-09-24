def chan(km):
    m = km*0.621371
    return m

km = int(input('킬로미터를 입력하세요 : '))
print ('%d킬로미터는 %.2f 마일이다.'%(km,chan(km)))