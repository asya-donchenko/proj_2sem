import sqlite3 

with sqlite3.connect('db/salary.db') as db: 
    cursor = db.cursor()

# создание таблицы Анкета

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS anketa (
        id INT AUTO_INCREMENT PRIMARY KEY,  
        name VARCHAR(30) NOT NULL,
        surname VARCHAR(30) NOT NULL,
        birht_date DATE NOT NULL,
        gender VARCHAR(1) NOT NULL,
        hire_date DATE NOT NULL,
        job_position VARCHAR(5) NOT NULL,
        otdel VARCHAR(50) NOT NULL,
        base_rate DECIMAL(6,2) NOT NULL
    )
    """)
    db.commit()

# создание таблицы Больничные листы 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hospitals_lists (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_person INT NOT NULL, 
        start_date DATE NOT NULL,
        finaly_date DATE NOT NULL,
        reason VARCHAR(1),
        diagnos VARCHAR(5),
        paid BOOLEAN,
        FOREIGN KEY (id_person) REFERENCES anketa(id)
    )
    """)
    db.commit()

with sqlite3.connect('db/salary.db') as db:
     cursor = db.cursor()

# Заполнение таблицы Анкета 
     cursor.execute("""INSERT INTO anketa VALUES(1, "Мария", "Фролова", "1990-05-08", "Ж", "2023-02-07", "Главный бухгалтер", "Бухгалтерия", "80500")""")
     cursor.execute("""INSERT INTO anketa VALUES(2, "Анастасия", "Лисовская", "1985-07-07", "Ж", "2023-06-08", "Бухгалтер", "Бухгалтерия", "32400")""")
     cursor.execute("""INSERT INTO anketa VALUES(3, "Максим", "Полухин", "1970-02-25", "М", "2019-04-13", "Менеджер продаж", "Отдел продаж", "150780")""")
     cursor.execute("""INSERT INTO anketa VALUES(4, "Анатолий", "Медведев", "1985-07-07", "М", "2020-06-08", "Юрист", "Юридический отдел", "55670")""")
     cursor.execute("""INSERT INTO anketa VALUES(5, "Виктор", "Широких", "1985-07-07", "М", "2021-06-15", "Помошник юриста", "Юридический отдел", "35700")""")
     cursor.execute("""INSERT INTO anketa VALUES(6, "Виктория", "Вяткина", "1985-07-07", "Ж", "2023-09-08", "Зам.директора", "Администрация", "89000")""")
     cursor.execute("""INSERT INTO anketa VALUES(7, "Елена", "Ларина", "1985-07-07", "Ж", "2018-07-21", "Бухгалтер", "Бухгалтерия", "32400")""")
     cursor.execute("""INSERT INTO anketa VALUES(8, "Ангелина", "Захаренко", "1985-07-07", "Ж", "2016-06-09", "Финансоый директор", "Финансовый отдел", "232680")""")
     cursor.execute("""INSERT INTO anketa VALUES(9, "Галина", "Сокол", "1985-07-07", "Ж", "2015-06-08", "Директор", "Администрация", "300500")""")
     cursor.execute("""INSERT INTO anketa VALUES(10, "Андрей", "Дмитров", "1985-07-07", "М", "2022-05-08", "Консультант", "Отдел продаж", "25080")""")
     db.commit()

#  Заполнение таблицы Больничные листы 
     cursor.execute("""INSERT INTO hospitals_lists VALUES(1, 1, "2023-06-06", "2023-07-23", "Трамва", "Перелом", TRUE)""")
     cursor.execute("""INSERT INTO hospitals_lists VALUES(2, 2, "2023-09-15", "2023-10-15", "Заболевание", "Грипп", FALSE)""")
     cursor.execute("""INSERT INTO hospitals_lists VALUES(3, 3, "2020-04-13", "2020-06-13", "Карантин", "Коронавирус", TRUE)""")
     cursor.execute("""INSERT INTO hospitals_lists VALUES(4, 4, "2021-06-08", "2021-07-08", "Трамва", "Перелом", TRUE)""")
     cursor.execute("""INSERT INTO hospitals_lists VALUES(5, 5, "2021-10-15", "2021-12-15", "Уход за больным", "отсутствует", FALSE)""")
     cursor.execute("""INSERT INTO hospitals_lists VALUES(6, 6, "2023-11-08", "2023-11-24", "Трамва", "Растяжение", FALSE)""")
     cursor.execute("""INSERT INTO hospitals_lists VALUES(7, 7, "2020-07-25", "2020-08-25", "Карантин", "Коронавирус", TRUE)""")
     cursor.execute("""INSERT INTO hospitals_lists VALUES(8, 8, "2018-08-09", "2018-10-09", "Заболевание", "Пневмония", TRUE)""")
     cursor.execute("""INSERT INTO hospitals_lists VALUES(9, 9, "2016-11-08", "2016-12-22", "Восстановление после операции", "аппендицит", FALSE)""")
     cursor.execute("""INSERT INTO hospitals_lists VALUES(10, 10, "2023-06-08", "2023-07-11", "Трамва", "Химический ожог", TRUE)""")
     db.commit()


with sqlite3.connect('db/salary.db') as db:
    cursor = db.cursor()
    print("Вывести список всех сотрудников и их должностей")

    for i in cursor.execute("""SELECT name, surname, job_position FROM anketa"""):
        print(i)


with sqlite3.connect('db/salary.db') as db:
    cursor = db.cursor()
    print("Вывести список всех сотрудников и их базовых ставок")

    for i in cursor.execute("""SELECT name, surname, base_rate FROM anketa"""):
        print(i)


with sqlite3.connect('db/salary.db') as db:
    cursor = db.cursor()
    print("Вывести список всех сотрудников, имеющих базовую ставку выше 100 000")

    for i in cursor.execute("""SELECT base_rate FROM anketa WHERE grade > 100000"""):
        print(i)
