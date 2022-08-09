import cv2
import os

from db_controller import insert_record
from validator import input_validator


# Path = path to QR code
# Return 'YYYY-MM-DD hh:mm'
def qr_decode(path):
    detect = cv2.QRCodeDetector()
    img = cv2.imread(path)
    value, points, straight_qrcode = detect.detectAndDecode(img)

    return value


# Insert all codes in qr_codes to DB
# In case any file in qr_codes is not a QR code of a date in format 'YYYY-MM-DD hh:mm'
# Print file name + value error
def insert_all_qr(connector, path='./qr_codes/'):

    for qr in os.listdir(path):
        date_from_qr = qr_decode(path+qr)
        try:
            date_to_insert = input_validator(date_from_qr)
            insert_record(connector, date_to_insert)
        except ValueError as e:
            print(f"{qr} {e}")
        finally:
            continue
