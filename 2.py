f=open("products.csv",encoding="utf-8-sig") # открываем наш файл, чтобы позже прочитать и обработать информацию в нем
s=f.readline() #считываем первую строку, содерж названия столбцов
#Category;product;Date;Price per unit;Count
A=[] # в этот список будем записывать полученную информацию о товарах
def sor(A):#Данная функция с помощью сортировки вставками в алфавитном порядке по категории сортирует полученные нами данные
    for i in range(len(A)):
        for j in range(i,0,-1):
            if A[j-1][0]>A[j][0]:
                A[j-1],A[j]=A[j],A[j-1]

for i in f:
    category,product,date,price_per,Count=[x for x in i.rstrip().split(';')]
    A.append([category,product,date,price_per,Count])
sor(A)
perv_cat=A[0][0] # ервая категория в отсортированной таблице
macostinformation=[] # информация про самый дорогой товар(категория,продукт,цена за шт)
macost=0 #макс цена из перв категории
for category,product,date,price_per,Count in A:
    if category==perv_cat and float(price_per)>macost:
        macost=float(price_per)
        macostinformation=[category,product,price_per]
print(f'В категории: {macostinformation[0]} самый дорогой товар: {macostinformation[1]} его цена за единицу товара составляет {macostinformation[2]}')

