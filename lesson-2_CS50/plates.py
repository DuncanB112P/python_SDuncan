def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = int(len(s))
    leading = s[0:2]

    for i in s:
        if not i.isalnum():
            return False

    for i, char in enumerate(s):
        if char.isdigit():
            first_digit_index = i
            for char in s[first_digit_index:]:
                if not char.isdigit():
                    return False
        else:
             break
    if s[first_digit_index] == '0':
        return False
    
    

    if length > 6:
        return False
    if length < 2:
        return False
    if not leading.isalpha():
        return False


    else:
        return True

main()