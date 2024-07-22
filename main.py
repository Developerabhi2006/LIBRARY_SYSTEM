import pandas as pd
from pymysql import connect
import mysql.connector as con
db = con.connect(user="root",password= "abhishek2006@",host= "localhost",database = "library_management_system")
cur = db.cursor()
d_b = connect(user = "root",password="abhishek2006@",database = "library_management_system")
cu_r=d_b.cursor()
def reg(a,b,c):
    if a==1:
        cur.execute("select count(id) from reader")
        z = cur.fetchone()
        m =  z[0]
        m= m+1
        cur.execute(f"insert into reader values({m},'{b}','{c}',null)")
        db.commit()
    elif a ==2:
        cur.execute("select count(id) from staff")
        z = cur.fetchone()
        m =  z[0]
        m= m+1
        cur.execute("insert into staff values({},'{}','{}')".format(m,b,c))
        db.commit()
def login(a,b):
    cur.execute(f"select*from reader where name ='{a}'and password='{b}'")
    c = cur.fetchone()
    if c :
        return True
    else :
        return False
def reader():
    print("what you  want")
    print("1.issue a book ")
    print("2. return a book ")
    a = int(input())
    if a == 1:
        cu_r.execute("select *from book_details")
        book_details= cu_r.fetchall()
        s = pd.DataFrame(book_details, columns = ["id","book_name","writer","Availablity"])
        print(s)
        book_req= input("NOT Founded the one u are looking for \n request the book here (y/n):")
        if book_req=='n'or book_req=='N':
            reqbook=input("Enter the book name :")
            reqwriter = input("Enter the writer name :")
            cur.execute("select count(id) from req_book")
            z = cur.fetchone()
            m =  z[0]
            m= m+1
            cur.execute(f"insert into req_book values ({m},'{reqbook}','{reqwriter}')")
            db.commit()
            print("your book will be added soon...../")
        else :
            b_id = input("Enter the id of the book u want to issue....")
            cur.execute(f"update  book_details set Availability = 'unavailable' where id = {b_id}")
            db.commit()
            print("BOOK ISSUED.............")
        ex= input("press enter to return to homepage..../")
        return ex 
    elif a ==2:
        b_id= input("enter the book id :")
        cur.execute(f"update book_details set Availability='available' where {b_id}= id ")
        db.commit()
        print("successful returned....")
        ex = input("press enter to return to homepage.../")
        return ex
def staff(a,b):
    cur.execute(f"select*from staff where name ='{a}'and password='{b}'")
    c = cur.fetchone()
    if c :
        print(f"WELLCOME {a} let's work".center(100,"*"))
        fu = int(input("1.ADD requsted book \n2.Remove a book form system....\n3.EXIT\n"))
        if fu==1:
            cu_r.execute("select*from req_book ")
            table = cu_r.fetchall()
            df = pd.DataFrame(table, columns = ["ID","NAME","WRITER"])
            print(df)
            print("1.ADD all")
            print("2.ADD one ")
            print("3.EXIT")
            s_in=int(input())
            if s_in==1:
                cur.execute("select count(id) from book_details")
                z = cur.fetchone()
                m =  z[0]
                m= m+1
                for i in table :
                    cur.execute(f"insert into book_details values({m},'{i[1]}','{i[2]}',default)")
                    db.commit()
                cur.execute("TRUNCATE TABLE req_book")
                print("DONE....")
            elif s_in ==2:
                onebook= int(input("Enter the ID of the book u want add :"))
                cur.execute(f"select*from req_book where id = {onebook}")
                data= cur.fetchone()
                cur.execute("select count(id) from book_details")
                z = cur.fetchone()
                m =  z[0]
                m= m+1
                cur.execute(f"insert into book_details values({m},'{data[1]}','{data[2]}',default)")
                db.commit()
                cur.execute(f"delete from req_book where id = '{onebook}'")
                db.commit()
                print("DONE...")
            elif s_in==3:
                print("DIRECTING TO HOMEPAGE...")
        elif fu==2:
            cu_r.execute("select *from book_details")
            book_details= cu_r.fetchall()
            s = pd.DataFrame(book_details, columns = ["id","book_name","writer","Availablity"])
            print(s)
            print("ENTER THE BOOK ID to remove..")
            bookremove= int(input())
            cur.execute(f"delete from book_details where id = '{bookremove}'")
        elif fu==3:
            print("DIRECTING TO HOMEPAGE")
def admin():
    cur.execute("select*from admin")
    admindata=cur.fetchone()
    username = input("ENTER YOUR USERNAME: ")
    PASSWORD = input("ENTER YOUR PASSWORD: ")
    if admindata[0]==username and admindata[1]==PASSWORD:
        print("WELLCOME ADMIN".center(40,"💀"))
        print("TELL US WHAT WE CAN DO ")
        print("1.SHUT DOWN")
        print("2.HELP")
        ad_choose= int(input())
        if ad_choose==1:
            cur.execute("drop database library_management_system")
            print("SERVISES CLOSED.../")
        elif ad_choose==2:
            print("You can use any of settings form reader or staff \njust login with your username and password")
            print("YOU CAN CLOSE THIS LIBRARY BY PRESSING 1")