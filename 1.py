f=open("products.csv",encoding="utf-8-sig") # открываем наш файл, чтобы позже прочитать и обработать информацию в нем
s=f.readline() #считываем первую строку, содерж названия столбцов
#Category;product;Date;Price per unit;Count
A=[] # в этот список будем записывать полученную информацию о товарах
for i in f:
    category,product,date,price_per,Count=[x for x in i.rstrip().split(';')]
    A.append([category,product,date,price_per,Count])
    total=float(price_per)*float(Count)
    A[-1].append(total)
Summa=0#итоговая сумма
for category,product,date,price_per,Count,total in A:
    if category=="Закуски":
        Summa+=total #постепенно считаем выручу за товары из категории Закуски
print(f'Итоговая сумма по категории Закуски {Summa}')
import csv
f2=open("products_new.csv",'w',newline='',encoding='utf-8-sig') #Запишем в этот файл обновленную информацию
writer=csv.writer(f2)
writer.writerow(["category","product","date","price_per","Count","total"]) #Запишем названия столбцов
writer.writerows(A) # запишем сами данные
f.close()
f2.close()