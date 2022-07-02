def spellCheck(word, key, accPercForCorr, caseSens):
    accuracy = 0
    total = len(key)
    if caseSens == False:
        w = word.lower()
        k = key.lower()
    else:
        w = w
        k = key

    if len(w) == len(k):
        print(f"+1 acc {len(w)}={len(k)}")
        accuracy += 1

    for i in range(len(w)):
        if w[i] == k[i]:
            accuracy += 1
            print(f"+1 acc {w[i]}{k[i]}")
        i += 1

    if round(accuracy/total,2) >= (accPercForCorr/100):
        print(f'{round(accuracy/total,2)} Same w')
    else:
        print(f'{round(accuracy/total,2)} Not same')

spellCheck('wammsbe', 'wannabe', 70, False)
