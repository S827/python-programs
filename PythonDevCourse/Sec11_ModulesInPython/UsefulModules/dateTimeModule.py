from time import time
import datetime

print(datetime.time())  # 00:00:00
print(datetime.time(8, 47, 50))  # can create time objects

# get the date
# returns 2024-09-03, tody's date in yyyy-mm-dd format
print(datetime.date.today())

# also the time module
t1 = time()
print(t1)
