import datetime

S = int(input())
td = datetime.timedelta(seconds=S)
m, s = divmod(td.seconds, 60)
h, m = divmod(m, 60)
print("{}:{}:{}".format(h, m, s))
