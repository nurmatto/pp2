import datetime 

now = datetime.datetime.now()
new_now = now.replace(microsecond=0)

print(now)
print(new_now)
