import pymysql as p
def getconnection():
    return p.connect(host="localhost",user="root",password="root",database="Blog")

def add_author_data(t):
    con=getconnection()
    db=con.cursor()
    db.execute('insert into authortable(a_uname,a_password,a_email,a_city) values(%s,%s,%s,%s)',t)
    con.commit()
    con.close()

def add_user_data(t):
    con=getconnection()
    db=con.cursor()
    db.execute('insert into usertable(u_uname,u_password,u_email,u_city) values(%s,%s,%s,%s)',t)
    con.commit()
    con.close()

def check_author_login(t):
    con=getconnection()
    db=con.cursor()
    db.execute('select a_uname from authortable where a_email=%s and a_password=%s',t)
    data=db.fetchone()
    db.close()
    if data:
        return data
    else:
        return False

def check_user_login(t):
    con=getconnection()
    db=con.cursor()
    db.execute('select u_uname from usertable where u_email=%s and u_password=%s',t)
    data=db.fetchone()
    db.close()
    if data:
        return data
    else:
        return False

def add_new_post(t):
    con=getconnection()
    db=con.cursor()
    db.execute('insert into author_post(p_uname,p_title,p_post) values(%s,%s,%s)',t)
    con.commit()
    con.close()

def all_author_view_post():
    con=getconnection()
    db=con.cursor()
    db.execute('select * from author_post')
    datalist=db.fetchall()
    db.close()
    return datalist

def author_view_post(t):
    con=getconnection()
    db=con.cursor()
    db.execute('select * from author_post where p_uname=%s',t)
    datalist=db.fetchall()
    db.close()
    return datalist