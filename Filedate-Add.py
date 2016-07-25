import time
import datetime

format = "%Y%m%d"

text = clipboard.get_selection()
date = datetime.datetime.now().strftime(format)

text = date + "_" + text

keyboard.send_key("<delete>")
keyboard.send_keys(text)