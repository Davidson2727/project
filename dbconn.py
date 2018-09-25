import mysqldb
#import mysql.connector



mydb = mysql.connector.connect(
    host = 'localhost',user='root',passwd='root',database='synth'
)

mycursor = mydb.cursor()

sql = 'INSERT INTO users (u_id varchar(255) NOT NULL, u_name varchar(255) NOT NULL, u_pass varchar(255) NOT NULL, email varchar(255) NOT NULL, PRIMARY KEY (u_id)) VALUES(%s,%s,%s,%s)'

val = ('01','jake','1234','email')

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
