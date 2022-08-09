from time import sleep
import platform
from plyer import notification
import winsound
import os


# Windows notifications
def play_sound():

    frequency = 1500  # Set Frequency To 1500 Hertz
    duration = 500  # Set Duration To 500 ms == 0.5 second
    winsound.Beep(frequency, duration)


def notify_win(date: str):
    play_sound()
    sleep(1)
    title = "Notification from KL"
    message = f"{date}"
    notification.notify(title=title,
                        message=message,
                        app_name="KL",
                        timeout=3,
                        toast=False)


# Mac notifications
def play_message(msg, voice="Victoria"):
    os.system(f'say -v {voice} {msg}')


def notify_mac(text, title="KL"):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
    play_message(text)


# Notification for Windows or Mac, else print
def notify(date: str):
    if platform.system() == 'Windows':
        notify_win(date)
    elif platform.system() == 'Darwin':
        notify_mac(date)
    else:
        print(date)
