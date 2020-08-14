# CREATION OF EMPLOYEE TABLE

import mysql.connector
con = mysql.connector.connect(host='18.219.99.141',database='db1',user='root',password='India12345')
c = con.cursor()
def create_table():
    c.execute("create table Ramya_EMPLOYEE(empno varchar(10),empname varchar(20),empsalary varchar(20))")
def insert_table():
    c.execute("insert into Ramya_EMPLOYEE values('001','Ramya','20,000')")
    c.execute("insert into Ramya_EMPLOYEE values('002','Rakshu','40,000')")
    c.execute("insert into Ramya_EMPLOYEE values('003','Deekshi','50,000')")
    c.execute("insert into Ramya_EMPLOYEE values('004','Varsha','10,000')")
    c.execute("insert into Ramya_EMPLOYEE values('005','Manoj','80,000')")
    con.commit()
def update_table():
    c.execute("update Ramya_EMPLOYEE set empname='Suraj',empsalary='40,0000' where empno='003'")
def delete_table():
    c.execute("delete from Ramya_EMPLOYEE where empname='Manoj'")
def select_table():
    c.execute('select * from Ramya_EMPLOYEE')
    dm=c.fetchall()
    for row in dm:
        print(row)
#create_table()
insert_table()
update_table()
delete_table()
select_table()
c.close()
con.close()



#CREATION OF PERSON TABLE

import mysql.connector
con = mysql.connector.connect(host='18.219.99.141',database='db1',user='root',password='India12345')
c = con.cursor()
def create_table():
    c.execute("create table Ramya_PERSON(name varchar(10),dob varchar(30),address varchar(20),pan varchar(20))")
def insert_table():
    c.execute("insert into Ramya_PERSON values('Ramya','12/04/2000','Banglore','12087865888')")
    c.execute("insert into Ramya_PERSON values('Nithin','12/06/1999','Kengeri','87954568887')")
    c.execute("insert into Ramya_PERSON values('Anitha','18/11/2000','KGF','74563456356')")
    c.execute("insert into Ramya_PERSON values('Lucky','01/08/2016','Mumbai','13591347707')")
    c.execute("insert into Ramya_PERSON values('Rum','13/12/2009','Chennai','98531346758')")
    con.commit()
def update_table():
    c.execute("update Ramya_PERSON set dob='11/08/2016',address='Mathikere',pan='898989898989' where name='Lucky'")
def delete_table():
    c.execute("delete from Ramya_PERSON where name='Rum'")
def select_table():
    c.execute('select * from Ramya_PERSON')
    dm=c.fetchall()
    for row in dm:
        print(row)
create_table()
insert_table()
update_table()
delete_table()
select_table()
c.close()
con.close()





#CREATION OF CAR TABLE

import mysql.connector
con = mysql.connector.connect(host='18.219.99.141',database='db1',user='root',password='India12345')
c = con.cursor()
def create_table():
    c.execute("create table Ramya_CAR(model varchar(30),num varchar(30),manu varchar(30),name varchar(30),price varchar(30))")
def insert_table():
    c.execute("insert into Ramya_CAR values('001','ka-04 mn-3092','maruthi','Maruthi','1,00,000')")
    c.execute("insert into Ramya_CAR values('002','ka-04 km-3045','swift','Maruthi','2,00,000')")
    c.execute("insert into Ramya_CAR values('003','ka-04 cn-3002','honda','swift','3,00,000')")
    c.execute("insert into Ramya_CAR values('004','ka-04 gm-4092','audi','audi','4,00,000')")
    c.execute("insert into Ramya_CAR values('005','ka-04 gn-8092','maruthi','Maruthi','1,00,000')")
    con.commit()
def update_table():
    c.execute("update Ramya_CAR set num='ka-09 ms-8987',manu='lamburgini',name = 'audi',price='8,00,000' where model='001'")
def delete_table():
    c.execute("delete from Ramya_CAR where model='005'")
def select_table():
    c.execute('select * from Ramya_CAR')
    dm=c.fetchall()
    for row in dm:
        print(row)
create_table()
insert_table()
update_table()
delete_table()
select_table()
c.close()
con.close()




#CREATION OF PRODUCT TABLE

import mysql.connector
con = mysql.connector.connect(host='18.219.99.141',database='db1',user='root',password='India12345')
c = con.cursor()
def create_table():
    c.execute("create table Ramya_PRODUCT(pid varchar(30),pname varchar(30),pdes varchar(100),pprice varchar(30))")
    print("cute")
def insert_table():
    c.execute("insert into Ramya_PRODUCT values('001','pen','blue pen writes well','25')")
    c.execute("insert into Ramya_PRODUCT values('002','rice','basumathi rice','1200')")
    c.execute("insert into Ramya_PRODUCT values('003','pencil','blue pencil well','30')")
    c.execute("insert into Ramya_PRODUCT values('004','kg card board','helps to do kids project','40')")
    c.execute("insert into Ramya_PRODUCT values('005','pen','blue pen writes well','25')")
    con.commit()
def update_table():
    c.execute("update Ramya_PRODUCT set pname='saree',pdes='kanchivaram silk saree',pprice = '25,000' where pid='002'")
def delete_table():
    c.execute("delete from Ramya_PRODUCT where pid='005'")
def select_table():
    c.execute('select * from Ramya_PRODUCT')
    dm=c.fetchall()
    for row in dm:
        print(row)
#create_table()
insert_table()
update_table()
delete_table()
select_table()
c.close()
con.close()