def main():
    x = get_int('What is x? ')      # Pass the prompt as the argument for the function
    print(f'x is {x}')

def get_int(prompt):        # When defining the function, all for the 'prompt' argument to be passed
    while True:
        try:
            return int(input(prompt))
        except ValueError:      # anticipating the user error (not providing an integer)
            pass
        

main()



