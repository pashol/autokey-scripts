import time
import datetime

format = "%H:%M"

date = datetime.datetime.now().strftime(format)

keyboard.send_keys(date)