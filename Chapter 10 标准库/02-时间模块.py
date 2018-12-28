import time

a = time.time()
print(a)
b = time.localtime()
print(b)
c = time.strftime('%Y-%m-%d %H:%M:%S')
print(c)


import datetime
d = datetime.datetime.now()
print(d)

new_time = datetime.timedelta(minutes=5)
print(new_time)
print(d + new_time)

one_day = datetime.datetime(2004,4,17)
new_date = datetime.timedelta(days=5)
print(one_day + new_date)