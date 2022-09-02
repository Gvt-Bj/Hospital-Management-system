import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="garvitx2c")
cur = mydb.cursor()
cur.execute('create database if not exists hospital')
cur.execute("use hospital")
mydb.commit()

doctor = '''
create table if not exists doctor(
Dno integer(5),
Dname varchar(20),
splst varchar(20),
MOB varchar(10),
ADR varchar(40))
'''
cur.execute(doctor)
mydb.commit()


def add_doctor():
    try:
        print('Enter the details :')
        s = 'insert into doctor (Dno, Dname, splst, MOB, ADR)' \
            'values(%s,%s,%s,%s,%s) '
        Dno = int(input('Enter Doctor no.: '))
        Dname = input('Enter Doctor name: ')
        splst = input('Enter speciality name: ')
        MOB = input('Enter MOB name: ')
        ADR = input('Enter ADR: ')
        value = (Dno, Dname, splst, MOB, ADR)
        cur.execute(s, value)
        print('Successfully added')
        mydb.commit()
        input('Press ENTER to continue.....')
    except:
        print('Error... try it again!!!')


def delete():
    try:
        Dname = input('Enter Doctor name you want to delete: ')
        s = "DELETE FROM doctor WHERE Dname = %s"
        value = (Dname,)
        cur.execute(s, value)
        mydb.commit()
        print('Successfully deleted!!!!!!')
        input('Press ENTER to continue.....')

    except:
        print('Error... try it again!!!')


def update():
    try:
        s = "update doctor set Dname= %s, splst= %s, MOB= %s, ADR= %s where Dno=%s"
        Dno = int(input('Enter Doc no.: '))
        Dname = input('Enter Doc name: ')
        splst = input('Enter speciality name: ')
        MOB = input('Enter MOB name: ')
        ADR = input('Enter ADR: ')
        value = (Dname, splst, MOB, ADR,Dno)
        cur.execute(s, value)
        mydb.commit()
        print("Successfully updated!!!!!!!!")
        input('Press ENTER to continue.....')

    except:
        print('Error... try it again!!!')


def see_details():
    s = 'select * from doctor'
    cur.execute(s)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    input('Press ENTER to continue.....')
