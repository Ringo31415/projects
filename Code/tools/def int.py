def Valid_float(a_string) :
    while True :
        try :
            a_float = float(input(f'{a_string}'))
            return a_float
        except :
            continue

a = Valid_float('Enter a:')
b = Valid_float('Enter b:')
