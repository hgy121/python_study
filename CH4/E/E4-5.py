total = 0
for i in range (1,101):
    if i%4==0:
        total += i
        print(f'{i} --> {total}')
        #print('{} --> {}'.format(i, total))

        