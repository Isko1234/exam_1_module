def sum_miss(list):
    n = len(list)
    if n ==0:
        return 0 
    if n == 1:
        return list[n-1]
    list.sort()
    start = list[0]
    end = list[n-1]
    sum = 0
    for i in range(start , end + 1):
        if i not in list:
            sum += i
    return sum
print(sum_miss([4 , 5  , 3 , 2  , 0]))