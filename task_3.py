def sort_grades(list):
    n = len(list)
    if n == 0:
        return '[]'
    for i in range(n):
        list[i]=list[i].upper()
    list.sort(reverse = True)
    return list
print(sort_grades(['b' , 'c' , 'C' , 'f' , 'A']))
