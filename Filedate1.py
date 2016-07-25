import time
import datetime

format = "%Y%m%d"

date = datetime.datetime.now().strftime(format)

keyboard.send_keys(date)