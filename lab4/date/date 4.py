import datetime 

nurma_birth_day = datetime.datetime(2006, 5, 4, 13, 4, 34, 56)
erbol_birth_day = datetime.datetime(1969, 1, 3, 5, 2, 20, 30)
difference = nurma_birth_day - erbol_birth_day
print(difference.total_seconds())