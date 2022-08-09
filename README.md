# Second Screening Task

## Table of contents
* [Installation](#installation)
* [Usage](#usage)

## Installation

```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```
The program takes all files from qr_codes as an input.
In case a file is not a QR code or a QR code without a valid date,
an error will be printed.

The notifications are built to either a Windows machine or a Mac machine.
In any other case the date will be printed.

In case the program is aborted before a date is notified,
it will be notified at the next run.
