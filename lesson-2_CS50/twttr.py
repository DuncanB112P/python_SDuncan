s = input('Input: ')
vowels = 'aeiouAEIOU'
new_string = ''

for i in s:
    if i not in vowels:
        new_string += i

print('Output:', new_string)


