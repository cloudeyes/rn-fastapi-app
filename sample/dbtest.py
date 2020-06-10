import os

dbtype = os.environ.get('DB_TYPE', 'mysql')
dbhost = os.environ.get('DB_HOST', 'localhost')
dbuser = os.environ.get('DB_USER', 'sample')
dbpass = os.environ.get('DB_PASS', 'sample')
dbname = os.environ.get('DB_NAME', 'sample')

print(f'{dbtype=}\n{dbhost=}\n{dbuser=}\n{dbname=}')

def mysql_test():
    import MySQLdb
    conn = MySQLdb.connect(dbhost, dbuser, dbpass, dbname)
    conn.query('SELECT version()')
    print(conn.use_result().fetch_row())
    conn.close()

def pgsql_test():
    import psycopg2
    conn = psycopg2.connect(dbname=dbname, user=dbuser, host=dbhost, password=dbpass)
    cur = conn.cursor()
    cur.execute('SELECT datname from pg_database')
    rows = cur.fetchall()
    print([it for it in rows])
    conn.close()

if __name__ == '__main__':
    if dbtype == 'mysql':
        mysql_test()
    elif dbtype == 'pgsql':
        pgsql_test()
