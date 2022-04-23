def get_ext(str):
    list = str.split('.')
    n = len(list)
    if n == 1 or n == 0 or list[0] == '' or list[1] == '':
        return ''
    else:
        return f'{list[n-1]}'
print(get_ext('file.py'))
