import datetime

today_is_great_day = datetime.datetime.today()
what_day_was_five_days_ago = datetime.timedelta(days=5)
five_days_ago = today_is_great_day.date()-what_day_was_five_days_ago
print(five_days_ago)