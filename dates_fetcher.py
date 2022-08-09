import datetime
import threading
from time import sleep

from db_controller import query_next_date, update_notified, all_notified
from notification import notify

# format = ('YYYY-MM-DD hh:mm', pk)
QUEUE = ''


# Set global variable queue to next date to be notified
# Return false if there are no dates to notify in DB
def next_date(connector) -> bool:

    global QUEUE
    date = query_next_date(connector)
    if date:
        formatted_date = f"{date[0][1]} {date[0][2]}"
        QUEUE = (formatted_date, date[0][0])
        return True
    else:
        return False


# While date in queue passed
# Send notification
# Update in DB
# Set next date in queue, if no next date->stop
# Sleep for 2 seconds to make sure all notifications can be seen
def notify_past_dates(connector, date_to_check):

    while QUEUE[0] <= date_to_check:
        notify(QUEUE[0])
        update_notified(connector, QUEUE[1])
        next_queue = next_date(connector)
        if not next_queue:
            break
        sleep(2)


# Every minute run a thread with current time to check and notify past dates
# If all dates in DB were notified -> Stop
def run_fetcher(connector):
    while True:
        current_date = str(datetime.datetime.today())[:-10]
        thread = threading.Thread(target=notify_past_dates, args=(connector, current_date))
        thread.start()
        thread.join()
        if all_notified(connector):
            break

        # make sure it runs every hh:mm:02
        current_second = datetime.datetime.today().second
        sleep_time = 62 - current_second
        sleep(sleep_time)
