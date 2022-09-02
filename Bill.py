def Bill_gen():
    import mysql.connector
    import random
    from datetime import datetime

    now = datetime.now()
    invoice = random.randint(1, 1000000)
    treatment = random.randrange(20000, 600000, 5000)
    bed = random.randrange(1000, 100000, 1000)
    tax = (treatment + bed) * 0.18
    total = treatment + bed + tax

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="9990")
    cur = mydb.cursor()
    cur.execute('create database if not exists hospital')
    cur.execute('use hospital')
    mydb.commit()
    pno = input('Enter Patient no.: ')
    s = 'select * from patient where pno = %s'
    value = (pno,)
    cur.execute(s, value)
    result = cur.fetchall()
    for rec in result:
        t = "patient-" + rec[1] + ".txt"
        with open(t, "w+") as f:
            f.write("                   Medical Receipt  \n\n")
            f.write(
                f'Date - {now} \t\t\t Invoice no.{invoice}\n\n')
            f.write(f"                  Patient details\n\n")
            f.write(
                f"Patient no.: {rec[0]}\nPatient name: {rec[1]}\nGender: {rec[2]}\nPatient age: {rec[3]}\nDisease: {rec[4]}\n")
            f.write(
                '======================================================================\n\n')
            f.write(
                f'Amount to be paid: {total}\nSummary - \nAmount charged for treatment: {treatment}\nBed charges: {bed}\nTax: {tax}\nTotal = {total}')
