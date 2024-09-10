pays = []
print('Amount due: 50')
coins = [5, 10, 25]

while True:
    x = int(input('Insert coin :'))
    if x not in coins:
        print('Amount Due: 50')
        pass
    else:  
        pays.append(x)
        paid = sum(pays)
        due = 50 - paid
        if due > 0:
            print('Amount Due:', due)
        elif due < 0:
            print('Change Owed:', paid - 50)
            break
        elif due == 0:
            print('Change Owed: 0')
            break





