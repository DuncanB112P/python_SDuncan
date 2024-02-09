#Practice calling function within function as means of organizing
# top to bottom code

'''
def main():
    x = input('response = ')
    print(convert(x))

def convert(answer):
    return answer.replace(':)', '🙂').replace(':(', '🙁')

main()

'''

def main():
    x = tip(input('Meal cost: '))
    print('Tip = ', x)

def tip(d):
    return float(d)

main()
