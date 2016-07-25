import time
import datetime

format = "%d.%m.%Y"

date = datetime.datetime.now().strftime(format)

keyboard.send_keys(date)