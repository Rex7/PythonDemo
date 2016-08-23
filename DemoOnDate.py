import datetime
import time
import calendar

curr = datetime.date
print("Today's date is :{0}".format(curr.today()))
print("year:"+str(curr.today().year))
print("day:"+str(curr.today().day))
print("month:"+str(curr.today().month))
print(curr.today().strftime("%d %b %y"))
time_now = time.time()
print("Time in formatted way :{0}".format(time.localtime(time_now)))
print("Time in mush pleasant way:", time.asctime())
print(calendar.month(1993, 2))
time.sleep(5)
print("slept for 5 seconds bitch")