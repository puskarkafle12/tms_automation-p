
import pytz
import datetime, time
# tms_time="11:59:59"
# today = datetime.datetime.now()
# t = datetime.datetime.strptime(tms_time,"%H:%M:%S")-datetime.datetime.strptime("2","%S")
# -datetime.datetime(today.year, today.month, today.day,11,00,00)
# ...and use datetime's hour, min and sec properties to build a timedelta
# delta = datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
# print(t)

# dt_now=datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)
# dt_mtn=dt_now.astimezone(pytz.timezone('Asia/Kathmandu'))
# print(dt_mtn)
# print(dt_now-dt_mtn)

# print(dt_mtn)
# dat=datetime.datetime.now()
# print(dat)
# # dat_east 
# dt = datetime.datetime(2013, 6, 2, 14, 36, 34, 383752)

# pause.until(dt)
# print('hello')
# # for tz in pytz.all_timezones:
# #     print(tz)
# today = datetime.datetime.strptime(tms_time,"%H:%M:%S")
# print(str(today))
# sleep = datetime.datetime(today.year, today.month, today.day, 11,00,00)
# print(today-sleep)
# driver.execute_script('document.getElementsByClassName("btn btn-sm ng-star-inserted")[0]").removeAttribute("disable");')
# driver.find_element_by_xpath("//button[@class='btn btn-sm ng-star-inserted']").click()
#to close the browser



import datetime
now = datetime.datetime.now()

if now.hour == 18 and now.minute == 25:
    print ('its time to eating lunch')
else :
    print ('its not the time for eating lunch')

tmstime='10:55:11'
today = datetime.datetime.strptime(tmstime,"%H:%M:%S")
var=(datetime.datetime(today.year, today.month, today.day, 10,59,58)-today).seconds
print(var)
if var<600:

     sleep = (datetime.datetime(today.year, today.month, today.day, 10,59,58) - today).seconds
     print('Waiting for ' + str(datetime.timedelta(seconds=sleep)))
     time.sleep(sleep)
else:
    print("runs without waiting")