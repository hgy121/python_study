year_sale = {'2016':237, '2017':98, '2018':158, '2019':233, '2020':120}

big = '2016'

for key in year_sale:
    if year_sale[key]> year_sale[big]:
        big = key

print('판매량이 가장 많은 해 : %s년'%big)
print('판매량 : %d대'%year_sale[big])