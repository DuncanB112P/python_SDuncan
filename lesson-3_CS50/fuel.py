while True:
    response = input('Fraction: ')
    num = response.split(sep='/')

    try:
        x = int(num[0])
        y = int(num[1])

        if x > y >= 1: 
            print('numerator cannot be larger than denominator')
        elif y == 0:
            print('denominator cannot be ZERO')
        else:
            pct = int(round(float(x/y*100), 0))
            if pct <= int(1):
                print('E')
            elif pct > int(98):
                print('F')
            else:
                print(pct, "%", sep='')
            break
    except ValueError:
        print('In fraction x/y, both x and y should be integers')



