import mysql.connector as c
con = c.connect(host = "localhost",user = "root",password = "honeychandu",database = 'project')
def show():
    cursor = con.cursor()
    cursor.execute(""" select * from sqlb;""")
    table = cursor.fetchall()
    con.commit()
    cursor.close()
    return table
def showPercentage(per):
    cursor = con.cursor()
    cursor.execute(""" select * from sqlb where Caste ="{per}";""".format(per =per))
    table = cursor.fetchall()
    con.commit()
    cursor.close()
    return table