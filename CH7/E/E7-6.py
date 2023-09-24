def count_al(sentence):
    global sm
    for i in sentence:
        if i == alphabet:
            sm += 1
    return sm


sm = 0
sentence = input('영어 문장을 입력하세요 : ')
alphabet = input('알파벳 하나를 입력하세요 : ')

print('%s 에 포함된 %s의 개수는 %d개이다.'%(sentence, alphabet,count_al(sentence)))