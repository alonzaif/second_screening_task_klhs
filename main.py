import threading

from QR_Reader import insert_all_qr
from dates_fetcher import run_fetcher, next_date
from db_controller import connect_db


# Main function
# Start and wait for a thread to insert all QR codes to DB
# Initialize queue
# If queue is not empty, start a thread to fetch dates
def main():

    con = connect_db()
    t1 = threading.Thread(target=insert_all_qr, args=(con,))
    t2 = threading.Thread(target=run_fetcher, args=(con,))
    t1.start()
    t1.join()

    date_in_queue = next_date(con)

    if date_in_queue:
        t2.start()
        t2.join()


if __name__ == '__main__':

    main()
