#Practice calling function within function as means of organizing
# top to bottom code

def main():
    x = input('response = ')
    print(convert(x))

def convert(answer):
    return answer.replace(':)', '🙂').replace(':(', '🙁')

main()