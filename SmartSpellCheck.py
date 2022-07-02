def ins(a,b,c):
    return a[:c]+b+a[c:]

def spellCheck(word, key, accPercForCorr, caseSens):
    accuracy = 0
    total = len(key)
    if caseSens == False:
        w = word.lower()
        k = key.lower()
    else:
        w = w
        k = key

    for i in range(len(w)):
        if w[i] == k[i]:
            accuracy += 1
            print(f"+1 acc {w[i]}{k[i]}")
        if w[i] == ' ':
            if k[i] != ' ':
                k = ins(k,' ',i)
        i += 1
    
    if len(w) == len(k):
        print(f"+1 acc {len(w)}={len(k)}")
        accuracy += 1

    if round(accuracy/total,2) >= (round(accPercForCorr/100, 2)):
        print(f'{round(accuracy/total,2)} Same word/phrase')
    else:
        print(f'{round(accuracy/total,2)} Not same word/phrase')

spellCheck('wamms be cool', 'wannabe cool', 70, False)
