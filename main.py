import csv
import random

with open('venv/books.csv','r',encoding='cp1251') as f:
    reader=csv.reader(f,delimiter=";")
    print("Ответ на первое задание: ", len(list(reader)))

with open("venv/books.csv","r",encoding="cp1251") as csvfile:
    reader=csv.reader(csvfile,delimiter=";")
    str_count=0
    for row in reader:
        if len(list(row[1]))>30:
            str_count+=1
    print("Ответ на второе задание: ",str_count)
search=input("Введите имя и фамилию  автора: ")
with open("venv/books.csv","r",encoding="cp1251") as csvfile1:
    reader=csv.reader(csvfile1,delimiter=";")
    flag=0
    for row in reader:
        rowToLower=row[3].lower()
        index=rowToLower.find(search.lower())
        #создаём массив, в котором ячейку с датой выпуска, разделяем знаком тире, чтобы можно было отделить год от дня и месяца.
        data=list(row[6].split("-"))
        if index!=-1 and int(data[0])<2016:
            flag=1
            print(row[3],"-",row[1],row[6])
    if flag==0:
        print("Ничего не найдено")

file=open("result.txt","w", encoding="utf-16")
with open('venv/books.csv','r',encoding='cp1251') as csvfile2:
    reader=csv.reader(csvfile2,delimiter=";")
    #считаем все строки
    count_st=0
    for row in reader:
        count_st+=1
with open('venv/books.csv','r',encoding='cp1251') as csvfile2:
    table=csv.reader(csvfile2,delimiter=";")
    #создаем массив, в который будем добавлять рандомные индексы строк
    randm_zp=[]
    table_file=list(table)
    for i in range(20):
        randm_zp.append(random.randint(0, count_st))
    count_nb=1
    randm_zp.sort()
    #проходимся по рандомным индексам и вписываем их в файл
    for j in randm_zp:
        file.write(str(count_nb) +". " + table_file[j][3] + ". " + table_file[j][1] + " " + "-" + " " + table_file[j][6][0:4]+"\n")
        count_nb+=1
file.close()
with open("venv/books.csv","r",encoding="cp1251") as csvfile3:
    table=csv.reader(csvfile3,delimiter=";")
    #созадем массив в который будем добавлять жанры
    janr_ms=[]
    for row in table:
        #создаем массив с жанром, разделенный #
        tags_m=row[12].split("#")
        for smv in tags_m:
            if smv not in janr_ms:
                janr_ms.append(smv)
print("Перечень всех тегов:")
print(", ".join(janr_ms[1:]))





























