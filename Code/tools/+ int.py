while True:
    try:
        N = int(input('Enter a positive integer:'))
        if N > 0:
            break
    except:
        continue
#make sure input is positive intger