print('-'*40)
print('     cm     mm     m     inch')
print('-'*40)

for cm in range(1,51):
    mm = cm*10
    m = cm*0.01
    inch = cm*0.3937
    print(f'{cm:6}{mm:6}{m:6.2f}{inch:6.2f}')

print('-'*40)