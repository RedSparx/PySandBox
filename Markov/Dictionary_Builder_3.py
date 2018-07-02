import re
import os
import numpy as np

def wTouples(Sentence,N):
    Words = Sentence.split()
    L=len(Words)-(N-2)
    for i in range(L-2):
        t=()
        for j in range(N):
            t+=(Words[i+j],)
        yield(t,Words[i+N])

def Show_Dict(D):
    for d in D:
        print('%50s ---> %-20s'%(d,D[d]))

if __name__=='__main__':
    Unique=0
    Not_Unique=0
    Order = 4
    Dictionary = {}
    os.chdir(r'Books\\')
    DB_Names=os.listdir()
    for FName in DB_Names:
        # print('Processing %s...'%FName)
        File = open(FName, encoding='utf8')
        Raw_Text=File.readlines()
        Text=' '.join([l.strip('\r\n') for l in Raw_Text])
        File.close()

        for Word_Touple,Nxt in wTouples(Text,Order):
            if Word_Touple in Dictionary.keys():
                Dictionary[Word_Touple].append(Nxt)
                Not_Unique+=1
            else:
                Dictionary[Word_Touple]=[Nxt]
                Unique+=1

    Sentence = []
    First_Word=False
    while First_Word==False:
        r=np.random.randint(0,len(Dictionary))
        Key=list(Dictionary.keys())[r]
        # print(Key)
        if (re.match(r'^[A-Z]',Key[0])):
            First_Word=True
    Sentence=list(list(Dictionary.keys())[r])
    Sentence.append(np.random.choice(Dictionary[Key]))

    # Show_Dict(Dictionary)
    Sentence_Complete=False
    for i in range(500):
        try:
            # print(Sentence)
            # print(tuple(Sentence[-Order:]))
            Next_Word = np.random.choice(Dictionary[tuple(Sentence[-Order:])])
            Sentence.append(Next_Word)
        except:
            print('xxxx')

    print('\n\n===>%s'%' '.join(Sentence))
