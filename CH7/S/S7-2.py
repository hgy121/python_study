eng_dict = {'house':'집', 'piano':'피아노', 'christmas':'크리스마스', 'friend':'친구', 'bread':'빵'}

def quiz(a):
     b = input('%s에 맞는 영어 단어는? ' %a)
     if eng_dict[b] == a:
         print('참 잘했어요!')
     else:
         print('틀렸어요!')


quiz('집')
quiz('피아노')
quiz('크리스마스')
quiz('친구')
quiz('빵')
 
