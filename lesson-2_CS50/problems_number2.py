# PROBLEM  2

media = [
    {'ext': 'gif', 'type': 'image/gif'},
    {'ext': 'jpg', 'type': 'image/jpeg'},
    {'ext': 'jpeg', 'type': 'image/jpeg'},
    {'ext': 'png', 'type': 'image/png'},
    {'ext': 'pdf', 'type': 'application/pdf'},
    {'ext': 'txt', 'type': 'test/plain'},
    {'ext': 'zip', 'type': 'application/zip'},
]


file_ext = input('Filename: ').lower().split('.')[-1]

media_types = [
    'gif',
    'jpeg',
    'jpg',
    'png',
    'pdf',
    'txt',
    'zip',
]

match file_ext:
    case 'gif' | 'jpeg' | 'jpg' | 'png' | 'pdf' | 'txt' | 'zip':
        for i in media:
            if i['ext'] == file_ext:
                print(i['type'])
    case _:
        print('application/octet-stream')



for n in filetypes:
    if n['ext'] == filename:
        print (n['type'])
    elif break:
        print('sorry')
    





