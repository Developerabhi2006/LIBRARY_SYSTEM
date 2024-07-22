import mysql.connector as con
import main
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
db = con.connect(user="root",password= "abhishek2006@",host= "localhost",database = "library_management_system")
if db :
    print("conneted")
    cur = db.cursor() 
    c = 'Y'
    z ='Y'
else :
    print("SERVICSES CLOSED")
try:
    while z == "y" or z== "Y":
        print(Fore.BLUE+"wellcome to our library".center(100,"="))
        print(Style.BRIGHT + "WHO ARE YOU........")
        print(Style.DIM+"1)Reader")
        print(Style.DIM+"2)Staff")
        print(Style.DIM+Fore.RED+"3)ADMIN")
        print(Style.BRIGHT + Back.BLUE+"4)NEW HERE.....?(want to register)")
        print(Style.DIM+"5)Exit")
        ex = 'Y'
        m = int(input(Style.BRIGHT+"waiting for your response :"))
        while ex =="y" or ex=="Y":
            if m == 4:
                print("Who are you ")
                print(Style.BRIGHT+"1)Reader")
                print(Style.DIM+"2)Looking for job register here ")
                a = int(input("Enter your choise: "))
                if a ==1:
                    b = input("Enter your username : ")
                    c = input("Enter your password : ")
                    main.reg(a,b,c)
                    p=input(Fore.GREEN+"Greate now let's read"+Fore.GREEN+"\npress enter to continue...")
                    print()
                    print()
                    break
                elif a ==2:
                    b = input("Enter your username : ")
                    c = input("Enter your password : ")
                    main.reg(a,b,c)
                    p=input(Fore.GREEN+"Greate now let's work"+Fore.GREEN+"\npress enter to continue...")
                    print()
                    print()
                    break
            elif m ==5:
                print(Fore.RED+"Thanks for visiting please visit again")
                ex ='z'
                z = 'z'
            elif m==1:
                print("wellcome reader please fill the cricredentials")
                a = input("enter your username :")
                b = input ("enter your password :")
                c = main.login(a,b)
                if c :
                    print(Style.BRIGHT + Fore.BLUE+Back.WHITE+f"WELLCOME BACK {a}".center(100,"*"))
                    ex = main.reader()              
                else :
                    print(Fore.RED+"INVALID usename or pass please try again ")
                    v = input("Press enter.....")
                    break
            elif m ==2:
                stffn = input("enter your staff name : ")
                stffp= input ("enter your password : ")
                ex = main.staff(stffn,stffp)
            elif m==3:
                main.admin()
except Exception:
    print("SOMETHING WENT WORNG")