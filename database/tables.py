from database.connection import DatabaseConfig

#function to create tables
def createTables():
    db_config = DatabaseConfig()
    #cursor object creation
    cursor = db_config.cursor()
    
    #tables query
    accounts_table_query= """create table if not exists accounts(
                      account int unsigned not null primary key, 
                      password varchar(30)
                    );"""
    
    users_table_query= """create table if not exists users (
                      userid int not unsigned null primary key, 
                      account int,username varchar(55) not null, 
                      email varchar(55) not null unique,
                      balance int unsigned not null,
                      created_at timestamp default current_timestamp,
                      foreign key (account) references accounts(account)
                    );"""

    transactions_table_query= """create table if not exists transactions (
                      transactionid int unsigned not null primary key, 
                      account int, 
                      transactiontype enum('DEBIT', 'CREDIT'), 
                      amount int not null, 
                      created_at timestamp default current_timestamp,
                      foreign key (account) references accounts(account)
                    );"""
    
    #execute the queries
    cursor.execute(accounts_table_query)
    cursor.execute(users_table_query)
    cursor.execute(transactions_table_query)

    db_config.commit()
    cursor.close()
    db_config.close()