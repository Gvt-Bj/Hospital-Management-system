import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="garvitx2c")
cur = mydb.cursor()
cur.execute('create database if not exists hospital')
cur.execute('use hospital')
mydb.commit()

Employee = '''
create table if not exists Employee(
Empno integer(20),
Empname varchar(20),
gender varchar(6),
age integer(100),
PhNo char(10))
'''
cur.execute(Employee)
mydb.commit()

def add_Employee():
    try:
        print('Enter the details :')
        s = 'insert into Employee (Empno, Empname, gender, age, PhNo)' \
            'values(%s,%s,%s,%s,%s) '
        Empno = int(input('Enter Employee no.: '))
        Empname = input('Enter Employee name: ')
        gender = input('Enter gender: ')
        age = input('Enter age: ')
        PhNo = input('Enter PhNo: ')
        value = (Empno, Empname, gender, age, PhNo)
        cur.execute(s, value)
        print('Successfully added')
        mydb.commit()
        input('Press ENTER to continue.....')
    except:
        print('Error... try it again!!!')


def delete():
    try:
        Empname = input('Enter Employee name you want to delete: ')
        s = 'DELETE FROM Employee WHERE Empname = %s'
        value = (Empname,)
        cur.execute(s, value)
        mydb.commit()
        print('Successfully deleted!!!!!!')
        input('Press ENTER to continue.....')

    except:
        print('Error... try it again!!!')


def update():
    try:
        s = "update Employee set Empname= %s, gender= %s, age= %s, PhNo= %s, where Empno= %s "
        Empno = int(input('Enter Employee no.: '))
        Empname = input('Enter Employee id: ')
        gender = input('Enter gender: ')
        age = input('Enter age: ')
        PhNo = input('Enter PhNo: ')
        value = (Empno, Empname, gender, age, PhNo,)
        cur.execute(s, value)
        mydb.commit()
        print("Successfully updated!!!!!!!!")
        input('Press ENTER to continue.....')

    except:
        print('Error... try it again!!!')


def see_details():
    s = 'select * from Employee'
    cur.execute(s)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    input('Press ENTER to continue.....')
