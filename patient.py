import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="garvitx2c")
cur = mydb.cursor()
cur.execute('create database if not exists hospital')
cur.execute('use hospital')
mydb.commit()

patient = '''
create table if not exists patient(
Pno integer(20),
Pname varchar(20),
gender varchar(6),
age integer(100),
PhNo char(10),
disease varchar(20))
'''
cur.execute(patient)
mydb.commit()


def add_patient():
    try:
        print('Enter the details :')
        s = 'insert into patient (Pno, Pname, gender, age, PhNo, disease)' \
            'values(%s,%s,%s,%s,%s,%s) '
        Pno = int(input('Enter Patient no.: '))
        Pname = input('Enter Patient name: ')
        gender = input('Enter gender: ')
        age = input('Enter age: ')
        PhNo = input('Enter PhNo: ')
        disease = input('Enter disease: ')
        value = (Pno, Pname, gender, age, PhNo, disease)
        cur.execute(s, value)
        print('Successfully added')
        mydb.commit()
        input('Press ENTER to continue.....')
    except:
        print('Error... try it again!!!')


def delete():
    try:
        Pname = input('Enter patient name you want to delete: ')
        s = 'DELETE FROM patient WHERE Pname = %s'
        value = (Pname,)
        cur.execute(s, value)
        mydb.commit()
        print('Successfully deleted!!!!!!')
        input('Press ENTER to continue.....')

    except:
        print('Error... try it again!!!')


def update():
    try:
        s = "update patient set Pname= %s, gender= %s, age= %s, PhNo= %s, disease= %s, where Pno= %s "
        Pno = int(input('Enter Patient no.: '))
        Pname = input('Enter Patient id: ')
        gender = input('Enter gender: ')
        age = input('Enter age: ')
        PhNo = input('Enter PhNo: ')
        disease = input('Enter disease: ')
        value = (Pno, Pname, gender, age, PhNo, disease)
        cur.execute(s, value)
        mydb.commit()
        print("Successfully updated!!!!!!!!")
        input('Press ENTER to continue.....')

    except:
        print('Error... try it again!!!')


def see_details():
    s = 'select * from patient'
    cur.execute(s)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    input('Press ENTER to continue.....')
