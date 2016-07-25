import time
import datetime

format = "%W"

date = datetime.datetime.now().strftime(format)

keyboard.send_keys(date)