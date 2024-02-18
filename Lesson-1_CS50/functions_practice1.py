
def main():
    x = int(input('What\'s x? '))
    print('x squared is', square(x))

def square(n):
    return n * n

main()

#############################################################################

def main():
    name = input('What\'s your name? ')
    hello(name)
    

def hello(to='world'):
    print('Hello,', to)

main()