def spellCheck(word, key, accPercForCorr):
    accuracy = 0
    total = len(key)

    if len(word) == len(key):
        print(f"+1 acc {len(word)}={len(key)}")
        accuracy += 1

    for i in range(len(word)):
        if word[i] == key[i]:
            accuracy += 1
            print(f"+1 acc {word[i]}{key[i]}")
        i += 1

    if round(accuracy/total,2) >= (accPercForCorr/100):
        print(f'{round(accuracy/total,2)} Same word')
    else:
        print(f'{round(accuracy/total,2)} Not same')

spellCheck('wammsbe', 'wannabe', 70)
