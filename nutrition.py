

fruit = input('Item: ').lower()

fruit_list = {
    'apple': '130',
    'avacado': '50',
    'banana': '110',
    'cateloupe': '50',
    'grapefruit': '60',
    'grapes': '90',
    'honeydew': '50',
    'kiwifruit': '90',
    'lemon': '15',
    'lime': '20',
    'nectarine': '60',
    'orange': '80',
    'peach': '80',
    'pear': '100',
    'pineapple': '50',
    'plums': '70',
    'strawberries': '50',
    'sweet cherries': '100',
    'tangerine': '50',
    'watermelon': '80'
}

for k,v in fruit_list.items():
    if fruit == k:
        print(v)
    else:
        pass


