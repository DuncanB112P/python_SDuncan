def main():
    x = input('response = ')
    print(convert(x))

def convert(answer):
    return answer.replace(':)', '🙂').replace(':(', '🙁')

main()