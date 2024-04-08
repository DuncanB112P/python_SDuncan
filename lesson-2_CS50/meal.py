def main():
    time = input('What is the time? ')
    t = convert(time)
    if t >= 7 and t <= 8:
        print('breakfast time')
    elif t >= 12 and t <= 13:
        print('lunch time')
    elif t >= 18 and t <= 19:
        print('dinner time')


def convert(n):
    t = n.split(':')
    h = int(t[0])
    m = int(t[1])
    converted = float(h + (m / 60))
    return converted

if __name__ == "__main__":
    main()
