f=open("products.csv",encoding="utf-8-sig") # открываем наш файл, чтобы позже прочитать и обработать информацию в нем
s=f.readline() #считываем первую строку, содерж названия столбцов
#Category;product;Date;Price per unit;Count
A=[] # в этот список будем записывать полученную информацию о товарах
from collections import defaultdict
def sor(A):#Данная функция с помощью сортировки вставками в алфавитном порядке по категории сортирует полученные нами данные
    for i in range(len(A)):
        for j in range(i,0,-1):
            if A[j-1][4]>A[j][4]:
                A[j-1],A[j]=A[j],A[j-1]
dd=defaultdict(lambda:0)
S=set()
B=[]
for i in f:
    category,product,date,price_per,Count=[x for x in i.rstrip().split(';')]
    A.append([category, product, date, price_per, Count])
sor(A)
for category,product,date,price_per,Count in A:
    B.append([product,Count])
     dd[product] = Count
c=0
for i in B:
    c+=1
    print(f'назв породукта {i[0]} "кол во {i[1]}')
    if c==10:
        break
