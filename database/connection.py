import mysql.connector as SQLC 

def DatabaseConfig():
    db_config = SQLC.connect(
        host='localhost',
        user='root',
        password='root',
        database='banknew'
    )
    return db_config