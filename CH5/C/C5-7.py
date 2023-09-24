s = [64,89,100,85,77,58,79,67,96,87,\
     87,36,82,98,84,76,63,69,53,22]
soo = 0
woo = 0
mi = 0
yang = 0
ga = 0

i = 0
while i<len(s):
    if 90<=s[i]<=100:
        soo += 1
    elif 80<=s[i]<90:
        woo +=1
    elif 70<=s[i]<80:
        mi +=1
    elif 60<=s[i]<70:
        yang +=1
    else:
        ga +=1
    i += 1
print('수 : %d명'%soo)
print('우 : %d명'%woo)
print('미 : %d명'%mi)
print('양 : %d명'%yang)
print('가 : %d명'%ga)