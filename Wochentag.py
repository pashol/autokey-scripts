import time
import datetime

format = "%A"

date = datetime.datetime.now().strftime(format)

keyboard.send_keys(date)