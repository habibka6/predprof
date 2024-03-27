f=open("products.csv",encoding="utf-8-sig") # открываем наш файл, чтобы позже прочитать и обработать информацию в нем
s=f.readline() #считываем первую строку, содерж названия столбцов
#Category;product;Date;Price per unit;Count
A=[] # в этот список будем записывать полученную информацию о товарах
for i in f:
    category,product,date,price_per,Count=[x for x in i.rstrip().split(';')]
    A.append([category,product,date,price_per,Count])
while True: # бесконечный цикл будет идти, пока не будет запроса "молоко"
    flag=0 # с помощью флага смотрим есть ли такая категория
    prod1="" # запоминает продукт
    counter1=1000000000000.0 #запоминает кол во
    zapros=input()#Запрос делаем\
    if zapros=="молоко":
        break
    for  category,product,date,price_per,Count in A:
       if category==zapros and float(Count)<counter1:
            flag =1
            prod1=product
            counter1=float(Count)
    if flag==0:
        print("Такой категории не существует в нашей БД")
    else:
        print(f'“В категории: {zapros} товар: {prod1} был куплен {counter1} раз”')


