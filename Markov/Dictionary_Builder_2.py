import re
import os
import numpy as np

def Pairs(Sentence):
    Words = Sentence.split()
    L=len(Words)-1
    for i in range(L):
        yield((Words[i],Words[i+1]))

def Triples(Sentence):
    Words = Sentence.split()
    L=len(Words)-2
    for i in range(L):
        yield((Words[i],Words[i+1],Words[i+2]))

def wTouples(Sentence,N):
    Words = Sentence.split()
    L=len(Words)-(N-2)
    for i in range(L-2):
        t=()
        for j in range(N):
            t+=(Words[i+j],)
        yield(t,Words[i+N])

if __name__=='__main__':
    Unique=0
    Not_Unique=0
    Order = 2
    Dictionary = {}
    os.chdir(r'Health-Tweets\\')
    DB_Names=os.listdir()
    for FName in DB_Names:
        # print('Processing %s...'%FName)
        File = open(FName, encoding='utf8')
        for line in File:
            line = re.sub(r'http\S+', '', line)
            Tweet = re.findall(r'[\w\-.\?\!\@\:\#\'\,\; ]+',line)[3]
            for Word_Touple,Nxt in wTouples(Tweet,Order):
                if Word_Touple in Dictionary.keys():
                    Dictionary[Word_Touple].append(Nxt)
                    Not_Unique+=1
                else:
                    Dictionary[Word_Touple]=[Nxt]
                    Unique+=1
        File.close()

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

    for i in range(8):
        try:
            Next_Word=np.random.choice(Dictionary[(Key[-1],Sentence[-1])])

        except:
            r = np.random.randint(0, len(Dictionary))
            Next_Word = list(Dictionary.keys())[r][0]
            # Next_Word=' '
        Sentence.append(Next_Word)

    print(' '.join(Sentence))