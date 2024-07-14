def main():
    subtotal = 0.00
    while True:
        try:
            sub = [ordering('Item: ')]
            for i in sub:
                subtotal += i
                print('Total: ', '$', f"{subtotal:.2f}", sep='')
        except EOFError:
            break
        except TypeError:
            pass


def ordering(prompt):

    order = input(prompt).lower()
   
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    try:
        for k,v in menu.items():
            if k.lower() == order:
                price = v
        return price
    except UnboundLocalError:
        pass
             
main()