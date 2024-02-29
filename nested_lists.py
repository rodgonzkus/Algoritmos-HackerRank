##### Nested Lists #####
if __name__ == '__main__':
    nestead_list = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nestead_list.append([name, score])
    nestead_list.sort()
    min_score = min([i[1] for i in nestead_list]) #Obtengo la nota min= 37.2
    sub_min_list = list() #Creo una lista nuevamente que no contenga la nota min   
    for i in nestead_list:
        if i[1] > min_score:
            sub_min_list.append(i)
    sub_min_score = min([i[1] for i in sub_min_list]) #Obtengo la nota min que no incluye el min anterior
    for i in nestead_list:
        if i[1] == sub_min_score:
            print(i[0]) #Obtengo el nombre de los alumnos que contienen el segundo min    