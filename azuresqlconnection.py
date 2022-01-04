import textwrap
import pyodbc

driver = '{ODBC Driver 17 for SQL Server}'

server_name = 'twitpoli1984-sqlsrv'
database_name = 'mosenatetweets-db'

server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)

username = "joewils"
password = "Pissyduck113!@"

connection_string = textwrap.dedent('''
    Driver={driver};
    Server={server};
    Database={database};
    Uid={username};
    Pwd={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
'''.format(
        driver=driver,
        server=server,
        database=database_name,
        username=username,
        password=password
))

cnxn: pyodbc.Connection = pyodbc.connect(connection_string)
crsr: pyodbc.Cursor = cnxn.cursor()

select_sql = "SELECT * From [mosenators]"
crsr.execute(select_sql)
print(crsr.fetchall())

insert_sql = "INSERT INTO [mosenators] (Senator, District, Party, Followers, UserDescription, StatusCount, Location) VALUES (?, ?, ?, ?, ?, ?, ?)"
records = [
    ('Joe Wilson', 'JD1', 'D', '238', 'Joe is not a senator', '6785', 'St. Louis'),
    ('Hayden', 'HD1', 'D', '228', 'Hayden is not a senator', '16785', 'Wentzville')
    ]



crsr.executemany(insert_sql, records)
crsr.commit()

cnxn.close()



#twitpoli1984-sqlsrv.database.windows.net
#Server=tcp:twitpoli1984-sqlsrv.database.windows.net,1433;Initial Catalog=mosenatetweets-db;Persist Security Info=False;User ID=joewils;Password={your_password};MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;