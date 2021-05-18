import sqlite3
import os



def func1(sql):
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.execute(sql)
    a = cursor.fetchall()
    print(a)
    connection.commit()
    return(a)
    connection.close()
    

    




while True:
    os.system('cls')
    print('1 - для добавки')
    print('2 - для просмотра')
    print('3 - для обновлять')
    a = input('Напиши цифру')
    
    if a == '1':
        text = input('Напиши текст')
        text1 = input()
        txt = f"INSERT INTO table_name (`column2`, `column3`) VALUES ('{text}', '{text1}');"
        func1(txt)
    elif a == '2':
        txt = "SELECT * FROM table_name;"
        func1(txt)
    elif a == '3':
        clm = input()
        text = input()
        txt = f"UPDATE table_name SET '{clm}' = '{text}' WHERE id = 1"
        func1(txt)
    else:
        print('Ты слепой')
