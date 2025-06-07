import datetime

x = datetime.datetime.now()
print(str(x).split()[0])

y = datetime.datetime(2000, 1, 1)
print(y)
print(y.strftime("%A"))