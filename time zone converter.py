import pytz, datetime

year=int(input("enter year"))
month=int(input("enter month"))
date=int(input("enter date"))
hours=int(input("enter hour"))
minutes=int(input("enter minutes"))

users_time=datetime.datetime(year,month,date,hours,minutes)

cairo_timezone=pytz.timezone('Africa/cairo')
Delhi_timezone=pytz.timezone('Asia/Kolkata')


cairo_time=pytz.utc.localize(users_time).astimezone(cairo_timezone)
print("cairo time is:",cairo_time.isoformat())



Delhi_time=pytz.utc.localize(users_time).astimezone(cairo_timezone)
print("Delhi time is:",Delhi_time.isoformat())
