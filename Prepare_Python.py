##### Say "Hello, World" with Python #####
string= "Hello, World!"
print(string)
##### Arithmetic Operators ######
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
##### Python Division #####
# a//b: Integer Division
# a/B: Float Division
a = 3; b= 5
print(f"Integer Division={a//b} and Float Division={a/b}")
##### Loops #####
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)
##### Write a Function #####
# Leap Year        
def is_leap(year):
    leap = bool()
    if year%4 ==0:
        leap=True
        if year%100==0:
            leap = False
            if year%400==0:
                leap = True
    return leap            
year = 1990
print(is_leap(year))
##### Print Function #####    
n = 3
numbers = []
for i in range(1,n+1):
    print(i)
    numbers.append(i)
print(*numbers, sep = "") 
##### Shape and Reshape #####
import numpy as np
#1. Usando Shape para obtener dimensiones de una matriz
my__1D_array = np.array([1, 2, 3, 4, 5])
print (my__1D_array.shape)     #(5,) -> 1 row and 5 columns
my__2D_array = np.array([[1, 2],[3, 4],[6,5]])
print (my__2D_array.shape)     #(3, 2) -> 3 rows and 2 columns 
#2. Usando Shape para cambiar las dimensiones de una matriz
change_array = np.array([1,2,3,4,5,6])
print(change_array.shape) #(6,) -> 1 row and 6 columns
change_array.shape = (3, 2) #Cambiamos la dimensión de la matriz de (6,) a (3,2)
print (change_array)
#3. Reshape crea una matriz con otras dimensiones y no modifica la matriz original en sí.
my_array = np.array([1,2,3,4,5,6])
print(my_array.shape)# (6,)
print (np.reshape(my_array,(3,2)))
#*. Dada una lista de 9 enteros separados por espacio (input()). Convertir esta lista en una matriz de 3x3
n = np.array(list(map(int, input().split())))
print(np.reshape(n, (3,3)))
##### Transpose and Flatten #####
#--------------------------------
##### Python If-Else #####
n=18
def if_else():
    if n%2!=0:
        print("Weird")
    if n%2==0 and n in range(6,21):
        print("Weird")    
    if n%2==0 and (n in range(2,6) or n > 20):
        print("Not Weird")
if_else()          

##### List Comprehensions #####
x=1; y=1; z=2; n=3
combinations_1 = list()
combinations_2 = list()
for a in range(0, x+1):
    for b in range(0,y+1):
        for c in range(0,z+1):
            if a+b+c != n:
                combinations_1.append([a,b,c])
            else:
                combinations_2.append([a,b,c])
print(combinations_1)               
#print(f"a+b+c !=3: {combinations_1}\nRemoved: {combinations_2}")                

##### Find the Runner-Up Score! ######
if __name__ == '__main__': #Runner-up: Subfinalista
    n = int(input()) # n scores
    arr = sorted(list(map(int, input().strip().split()))) #Un vector de dimensión n separados por espacio que fué converitido en una lista ordenada
    max_arr = max(arr)
    sub_max_arr = list()
    for i in arr:
        if i < max_arr:
            sub_max_arr.append(i)
    print(max(sub_max_arr))        

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


##### Finding the percentage #####
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_means = {}
    for k,v in student_marks.items():
        scores_average = sum(v)/len(v)
        student_means[k] = scores_average 
    print("%.2f" % round(student_means[query_name], 2)) #Formato para que aparezca con dos decimales

    
##### Standardize Mobile Number Using Decorators #####
def wrapper(f):
    def fun(l):
        decorated_l = ['+91 {} {}'.format(n[-10: -5], n[-5:]) for n in l]
        return f(decorated_l)
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')
if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


###### Tuples #####
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
##### XML 1 - Find the Score #####










 