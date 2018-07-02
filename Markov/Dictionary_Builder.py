import re
import os

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
    L=len(Words)-(N-1)
    for i in range(L):
        t=()
        for j in range(N):
            t+=(Words[i+j].lower(),)
        yield(t)

def Next_Word(Word_Touple):
    print(Dictionary[Word_Touple])

if __name__=='__main__':
    Unique=0
    Not_Unique=0
    Order = 2
    Dictionary = {}
    os.chdir(r'Health-Tweets\\')
    DB_Names=os.listdir()
    for FName in DB_Names:
        print('Processing %s...'%FName)
        File = open(FName, encoding='utf8')
        for line in File:
            line = re.sub(r'http\S+', '', line)
            Tweet = re.findall(r'[\w\-.\?\!\@\:\#\'\,\; ]+',line)[3]
            for Word_Touple in wTouples(Tweet,Order):
                if Word_Touple in Dictionary.keys():
                    Dictionary[Word_Touple]+=1
                    Not_Unique+=1
                else:
                    Dictionary[Word_Touple]=1
                    Unique+=1
        File.close()
    print('Unique:\t\t\t%d\nNot Unique:\t\t%d'%(Unique,Not_Unique))
    print(Next_Word(('many','doctors')))
    # print(Dictionary)
