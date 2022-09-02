import doctor
import patient
import Employee as employee
import Bill_db
from os import system, name
from time import sleep


def clear():
    return system('cls')


while True:
    clear()
    print("\t\t\t Hospital Manangement program\n")
    print("===================================================")
    print("1.Doctor management")
    print("2.Patient management")
    print('3.Bill')
    print('4.Employee management')
    print("5.Exit")
    choice = int(input("enter choice between 1 to 3---->"))
    while choice == 1:
        clear()
        print("\t\t\t Doctor Record Management\n")
        print("===========================================================================")
        print("1.Add Doctor Record")
        print("2.Display Doctor Records")
        print("3.Delete Doctor Records")
        print("4.Update Doctor Record")
        print("5.Return to Main Menu")
        print("===========================================================================")
        choice = int(input("enter choice between 1 to 5-->"))
        if choice == 1:
            clear()
            doctor.add_doctor()
            clear()
            continue
        elif choice == 2:
            clear()
            doctor.see_details()
            clear()
            continue
        elif choice == 3:
            clear()
            doctor.delete()
            clear()
            continue
        elif choice == 4:
            clear()
            doctor.update()
            clear()
            continue
        elif choice == 5:
            break
        else:
            print("wrong choice.....enter your choice again")
            clear()
            continue
        continue

    while choice == 2:
        print("\t\t\t Patient Record Management\n")
        print("===========================================================================")
        print("1.Add Patient Record")
        print("2.Display Patient Records")
        print("3.Delete Patient Records")
        print("4.Update Patient Record")
        print("5.Return to Main Menu")
        print("===========================================================================")
        choice = int(input("enter choice between 1 to 5-->"))
        if choice == 1:
            clear()
            patient.add_patient()
            clear()
            continue
        elif choice == 2:
            clear()
            patient.see_details()
            clear()
            continue
        elif choice == 3:
            clear()
            patient.delete()
            clear()
            continue
        elif choice == 4:
            clear()
            patient.update()
            clear()
            continue
        elif choice == 5:
            break
        else:
            print("wrong choice.....enter your choice again")
            continue
        continue
    while choice == 3:
        print("\t\t\t Bill Management\n")
        print("===========================================================================")
        print("1.Add Bill")
        print("2.Delete Bill Records")
        print("3.Display Bill Records")
        print("4.Update Bill Record")
        print("5.Return to Main Menu")
        print("===========================================================================")
        choice = int(input("enter choice between 1 to 5-->"))
        if choice == 1:
            clear()
            Bill_db.add_Bill()
            clear()
            continue
        elif choice == 2:
            clear()
            Bill_db.delete()
            clear()
            continue
        elif choice == 3:
            clear()
            Bill_db.see_details()
            clear()
            continue
        elif choice == 4:
            clear()
            doctor.update()
            clear()
            continue
        elif choice == 5:
            break
        else:
            print("wrong choice.....enter your choice again")
            clear()
            continue
        continue
    while choice == 4:
        print("\t\t\t Employee Management\n")
        print("===========================================================================")
        print("1.Add a new employee")
        print("2.Delete employees")
        print("3.Update employees")
        print("4.View employee details")
        print("5.Return to Main Menu")
        print("===========================================================================")
        choice = int(input("enter choice between 1 to 5-->"))
        if choice == 1:
            clear()
            employee.add_Employee()
            clear()
            continue
        elif choice == 2:
            clear()
            employee.delete()
            clear()
            continue
        elif choice == 3:
            clear()
            employee.update()
            clear()
            continue
        elif choice == 4:
            clear()
            employee.see_details()
            clear()
            continue
        elif choice == 5:
            break
        else:
            print("wrong choice.....enter your choice again")
            continue
        continue
    if choice == 5:
        break
    else:
        print("wrong choice....enter your choice again")
        continue
