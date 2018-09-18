import sqlite3
import time
# '''创建一个数据库，文件名'''
conn = sqlite3.connect('./Contact.db')
# '''创建游标'''
cursor = conn.cursor()

# '''执行语句'''
def create():
    sql = '''create table Contact (
        stdName text,
        phoneNum int,
        birthPlace text,
        idNum text,
        gender text)'''

    cursor.execute(sql)

    print("Table created")

# '''使用游标关闭数据库的链接'''
    cursor.close()
    conn.close()

#加入新學生 需要輸入信息
def insert():
    conn = sqlite3.connect('Contact.db')
    cursor = conn.cursor()
    print("Connected")

    name1 = str(input("Please enter the name of student: "))
    pNum1 = str(input("Please enter the phone number of student: "))
    bPlc1 = str(input("Please enter the birthplace of student: "))
    idNum1 = str(input("Please enter the id number of student: "))
    gen1 = str(input("Please enter the gender of student(M for male and F for female): "))
    sql = '''insert into Contact
            (stdName, phoneNum, birthPlace, idNum, gender)
            values
            (:name, :pNum, :bPlc, :idNum, :gen)'''
    cursor.execute(sql,{'name':name1, 'pNum':pNum1, 'bPlc':bPlc1, 'idNum':idNum1, 'gen':gen1})
    conn.commit()

    cursor.close()
    conn.close()
    print("Student Added")

#女生數量+男生出生在台北的學號
def select_q3():
    conn = sqlite3.connect('Contact.db')
    cursor = conn.cursor()

    print("Connected")
    sql = '''select count() from Contact where gender = 'F';'''
    sql2 = '''select idNum from Contact where gender = 'M' AND birthPlace = 'Taipei';'''
    results = cursor.execute(sql)
    noob = str(results.fetchall())
    print("Number of females: " + noob)
    results2 = cursor.execute(sql2)
    come = results2.fetchall()
    print("ID of Males who live in Taipei")
    for comes in come:
        print(comes)

    results.close()
    results2.close()
    conn.close()

#出生地
def select_q4():
    conn = sqlite3.connect('Contact.db')
    cursor = conn.cursor()

    print("Connected")
    sql = '''select distinct birthPlace from Contact;'''
    results = cursor.execute(sql)
    all_words = results.fetchall()
    for word in all_words:
        print(word)

    results.close()
    conn.close()

#輸入學號之後進行更改
def update():
    conn = sqlite3.connect('Contact.db')
    cursor = conn.cursor()
    print("Connected")

    choice = str(input("Please enter the id number of the student you want to update: "))
    print("1. Name")
    print("2. Phone Number")
    print("3. Birth Place")
    print("4. Id Number")
    print("5. Gender")
    choice2 = str(input("What info do you want to update?"))
    udInfo = str(input("Please enter the new info: "))
    if choice2 == '1':
        sql = '''update Contact set stdName = ? where idNum = ?;'''
        cursor.execute(sql,[udInfo,choice])
    elif choice2 == '2':
        sql = '''update Contact set phoneNum = ? where idNum = ?'''
        cursor.execute(sql,[udInfo,choice])
    elif choice2 == '3':
        sql = '''update Contact set birthPlace = ? where idNum = ?'''
        cursor.execute(sql,[udInfo,choice])
    elif choice2 == '4':
        sql = '''update Contact set idNum = ? where idNum = ?'''
        cursor.execute(sql,[udInfo,choice])
    elif choice2 == '5':
        sql = '''update Contact set gender = ? where idNum = ?'''
        cursor.execute(sql,[udInfo,choice])
    conn.commit()

    cursor.close()
    conn.close()
    print("Info Updated")

#輸入學號刪除該學生資料
def delete():
    conn = sqlite3.connect('Contact.db')
    cursor = conn.cursor()
    print("Connected")

    id = str(input("Please enter the id of the student you want to delete: "))
    sql = '''delete from Contact where idNum = ?'''
    cursor.execute(sql,[id])
    conn.commit()

    cursor.close()
    conn.close()
    print("Student deleted")

#顯示當前通訊錄內容
def show():
    conn = sqlite3.connect('Contact.db')
    cursor = conn.cursor()
    print("Connected")

    sql = '''select * from Contact'''
    result = cursor.execute(sql)
    all_data = result.fetchall()
    for data in all_data:
        print(data)


    cursor.close()
    conn.close()

i = 0
while i <1:
    print("0. Create table")
    print("1. Check the current table")
    print("2. Insert a new student's info")
    print("3. Check how many females & List of idNum of males who live in Taipei")
    print("4. Check what places the students are from")
    print("5. Update a student's info")
    print("6. Delete a student's info")
    print("7.Exit")
    operation = str(input("Please enter what you want to do: "))
    if operation =='0':
        create()
    elif operation == '1':
        show()
    elif operation == '2':
        insert()
    elif operation == '3':
        select_q3()
    elif operation =='4':
        select_q4()
    elif operation == '5':
        update()
    elif operation == '6':
        delete()
    elif operation =='7':
        i = 1