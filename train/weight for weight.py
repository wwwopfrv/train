def order_weight(strng):
    order = strng.split(',')
    for i in range(len(order)):
        for j in range(len(order)):
            first = sum(list(map(int,order[i])))
            second = sum(list(map(int,order[j])))
            if first > second or first == second:
                w = order[i]
                order[i] = order[j]
                order[j] = w
            elif first < second:
                w = order[j]
                order[j] = order[i]
                order[i] = w
    return''.join(order)


print(order_weight('3,4,-1,12,98'))
    
                    
                