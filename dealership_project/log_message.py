from datetime import datetime


def log(message):
    timestamp_format = '%H:%M:%S-%h-%d-%Y'  # Hour-Minute-Second-MonthName-Day-Year
    now = datetime.now()  # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open('dealership_log_file.txt', 'a') as f:
        f.write(timestamp + ',' + message + '\n')
