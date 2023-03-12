import zhdate
import datetime

#阴历转阳历
lsdate = zhdate.ZhDate(2006,6,29)
#print(lsdate)
print(lsdate.to_datetime())

#阳历转阴历
lsdate2 = datetime.datetime(2006,6,29)
#print(lsdate2)
print(zhdate.ZhDate.from_datetime(lsdate2))