item_count = {}
while True:
    try:
        x = input().upper()

        if x in item_count:
            item_count[x] += 1
        else:
            item_count[x] = 1
    except (KeyboardInterrupt, EOFError):
        break

for item in sorted(item_count):
    print(item_count[item], item)





 







    


