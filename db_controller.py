import sqlite3 as sl

SQL_INSERT = "INSERT INTO DATE (date, time, notified) values(?, ?, ?)"
SQL_NEXT_DATE = "SELECT * FROM DATE WHERE notified = False ORDER BY date ASC, time ASC LIMIT 1"
SQL_UPDATE = "UPDATE DATE SET notified = True WHERE id = {}"
SQL_QUERY_DONE = "SELECT * FROM DATE WHERE notified = False"


# Save dates to DB
# Data = ['YYYY-MM-DD', 'hh:mm']
# Date to insert = ('YYYY-MM-DD', 'hh:mm', False)
def insert_record(connector, data: list):
    data.append(False)
    date_to_insert = tuple(data)
    with connector:
        connector.execute(SQL_INSERT, date_to_insert)


# Return earliest date that was not notified
def query_next_date(connector):
    with connector:
        data = connector.execute(SQL_NEXT_DATE)
        row = data.fetchall()
        return row


# Change date row to notified
def update_notified(connector, idx):
    with connector:
        connector.execute(SQL_UPDATE.format(idx))


# Query all not notified dates
# Return True for empty
def all_notified(connector) -> bool:
    data = connector.execute(SQL_QUERY_DONE)
    if data.fetchone():
        return False
    else:
        return True


# Connect to DB, create DB in case it was not existed
# Create table "DATE", if not existed
# Return DB-controller
def connect_db():
    con = sl.connect('dates.db', check_same_thread=False)

    with con:
        con.execute("""
                    CREATE TABLE IF NOT EXISTS DATE (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        date TEXT,
                        time TEXT,
                        notified BOOL
                    );
                """)

    return con
