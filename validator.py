import datetime


# Validate input 'YYYY-MM-DD hh:mm'
# Validate date exists
# Return ['YYYY-MM-DD', 'hh:mm']
def input_validator(date: str) -> list:

    try:
        valid_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
        return date.split()
    except:
        raise ValueError("Not a valid input")
