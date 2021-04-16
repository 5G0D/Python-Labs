import itertools as it

anws = []
n = int(input())
word = input()
word = list(word)

if n > len(word):
    perem = n - len(word)
    b = list(it.permutations(word, perem))
    
    for i in b:
        for j in i:
            word.append(j)
            
        a = [el for el in it.permutations(word, n)]
        
        for i in range (len(a)):
            anws.append(''.join(map(str, a[i])))
            
        del word[len(word)::]
        
    h = list(set(anws))
    
    for g in range(len(h)):
        print(h[g], end=' ')
else:
    for i in list(it.permutations(word, n)):
        print(''.join(map(str, i)), end = ' ')
