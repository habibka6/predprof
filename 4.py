#Промокод должен состоять из первых 2-ух букв названия + день поступления
# + 2 предпоследних буквы названия в обратном порядке + месяц поступления в обратном порядке.
import csv
def prom(product,data):
    return (product[:2]+data[:2]+product[-1]+product[-2]+data[4]+data[3])
f=open("products.csv",encoding="utf-8-sig") # открываем наш файл, чтобы позже прочитать и обработать информацию в нем
s=f.readline() #считываем первую строку, содерж названия столбцов
#Category;product;Date;Price per unit;Count
A=[] # в этот список будем записывать полученную информацию о товарах
for i in f:
    category,product,date,price_per,Count=[x for x in i.rstrip().split(';')]
    A.append([category,product,date,price_per,Count])
    promocod=prom(product,date)
    A[-1].append(promocod)
f2=open('product_promo.csv','w',newline='',encoding='utf-8-sig')
writer=csv.writer(f2)
writer.writerow(["category","product","date","price_per","Count","promocod"])
writer.writerows(A)