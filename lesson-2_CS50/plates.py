def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = int(len(s))
    leading = s[0:2]
    num_found = False

    if length < 2 or length > 6:
        return False
    elif not leading.isalpha():
        return False
    

    for i in s:
        if not i.isalnum():
            return False
        
        if i.isdigit():
            if i == '0' and not num_found:
                return False
            num_found = True

        elif num_found:
            return False

    return True

    

main()