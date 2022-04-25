while True:
    try:
        s1 = str(input('Please input one word: '))
        if s1.isalpha() == True:
            break
    except:
        continue