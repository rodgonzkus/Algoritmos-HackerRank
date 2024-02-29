##### Find the Runner-Up Score! ######
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().strip().split())
    arr = sorted(list(arr)) #arr será entendido como un vector o una lista de dimensión n separados por espacio que fué converitido en una lista ordenada
    max_arr = max(arr)
    sub_max_arr = list()
    for i in arr:
        if i < max_arr:
            sub_max_arr.append(i)
    print(max(sub_max_arr))    
    