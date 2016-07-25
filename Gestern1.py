import datetime

format = "%d.%m.%Y"

date = datetime.datetime.now()
date = date - datetime.timedelta(days=1)
date = date.strftime(format)

keyboard.send_keys(date)