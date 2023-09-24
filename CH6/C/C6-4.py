words = {'꽃':'flower','나비':'butterfly','학교':'school','자동차':'car'}

print('<영어 단어 맞추기 퀴즈>')

for kor in words:
    input_word = input("'%s'에 해당되는 영어 단어를 입력해주세요: "%kor)

    if words[kor] == input_word:
        print('정답')
    else:
        print('오답')