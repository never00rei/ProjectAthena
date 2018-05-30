from os import getenv

def setup():
    PGUSER = getenv('PGUSER', 'athena')
    PGHOST = getenv('PGHOST', 'localhost')
    PGPORT = getenv('PGPORT', 5433)
    PGPASS = getenv('PGPASS', 'athena')
    PGDATABASE = getenv('PGDATABASE', 'application')

    db_url = f'postgresql://{PGUSER}:{PGPASS}@{PGHOST}:{PGPORT}/{PGDATABASE}'

    return db_url