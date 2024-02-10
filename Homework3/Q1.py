# Write code that prints the current time in this format: (hour:minutes:seconds)
# example:  15:58:19
>>> from datetime import datetime
>>> #get the current time
>>> current_time = datetime.now().time()
>>> #format the current time as hour:minutes:seconds
>>> formatted_time = current_time.strftime("%H:%M:%S")
>>> # print the formatted time
>>> print("current time:", formatted_time)
current time: 12:12:17
