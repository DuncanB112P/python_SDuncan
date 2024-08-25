response = input('camelCase: ')

res = ""


for i in response:
     if i.isupper():
          res += "_" + i
     else:
          res += i



print(res.lower())


