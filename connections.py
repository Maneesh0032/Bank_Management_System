import mysql.connector as SQLC # type: ignore


db_config = SQLC.connect(
    host='localhost',
    user='root',
    password='root',
    database='banknew'
)
cursor = db_config.cursor()
print("Database connection successful!")
print(db_config)
print(cursor)

cursor.execute("create database if not exists banknew1;")
cursor.execute("use banknew1;")
cursor.execute("create table if not exists users (acc_id int auto_increment primary key, name varchar(255) not null,amount int);")
print(cursor)