import mysql.connector
import patient

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="garvitx2c")
cur = mydb.cursor()
cur.execute('create database if not exists hospital')
cur.execute('use hospital')
mydb.commit()

Bill_db = '''
create table if not exists Bill(
Bill_no int,
Bill_name varchar(20),
PhNo varchar(10))
'''
cur.execute(Bill_db)
mydb.commit()

def add_Bill():
    try:
        print('Enter the details :')
        s = 'insert into Bill (Bill_no, Bill_name, PhNo)' \
            'values(%s,%s,%s) '
        Bill_no = int(input('Enter Bill no.: '))
        Bill_name = input('Enter Bill name: ')
        PhNo = input('Enter PhNo: ')
        value = (Bill_no, Bill_name, PhNo)
        cur.execute(s, value)
        print('Successfully added')
        mydb.commit()
        input('Press ENTER to continue.....')
    except:
        print('Error... try it again!!!')


def delete():
    try:
        Bill_name = input('Enter Bill_no name you want to delete: ')
        s = 'DELETE FROM Bill_no WHERE Bill_name = %s'
        value = (Bill_name,)
        cur.execute(s, value)
        mydb.commit()
        print('Successfully deleted!!!!!!')
        input('Press ENTER to continue.....')

    except:
        print('Error... try it again!!!')


def update():
    try:
        s = "update Bill set Bill_name= %s, PhNo= %s where Bill_no= %s "
        Bill_no = int(input('Enter Bill_no: '))
        Bill_name = input('Enter Bill name: ')
        PhNo = input('Enter PhNo: ')
        value = (Bill_name, PhNo, Bill_no)
        cur.execute(s, value)
        mydb.commit()
        print("Successfully updated!!!!!!!!")
        input('Press ENTER to continue.....')

    except:
        print('Error... try it again!!!')


def see_details():
    s = 'select * from Bill'
    cur.execute(s)
    result = cur.fetchall()
    for rec in result:
        print(rec)
    input('Press ENTER to continue.....')
