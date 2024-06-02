# Find the no of seconds in a given year
print("Seconds in a given yr Calculator")

yr = int(input("Enter the year: "))
days_in_yr = 365
hrs_in_day =  24
mins_in_hr = 60
secs_in_min = 60

if yr%100 == 0 or yr%400 == 0 or yr%4 == 0:
  days = days_in_yr + 1
  
else:
  days = days_in_yr

secs =  days * hrs_in_day * mins_in_hr * secs_in_min
print(secs)
