print('-'*40)
print('     cm     mm    m    inch')
print('-'*40)
cm = 1

while cm<=50:
    mm = cm*10
    m = cm*0.01
    inch = cm*0.3937
    print(f'{cm:6}{mm:6}{m:6.2f}{inch:6.2f}')
    cm += 1
print('-'*40)