question = ['s_hool','compu_er','seco_ation','windo_','hi_tory']
answers = ['c','t','r','w','s']

for i in range(0,len(question)):
    q = '%s:밑 줄에 들어갈 알파벳은?'%question[i]
    guess = input(q)

    if guess == answers[i]:
        print('정답!')
    else:
        print('틀렸어요!')