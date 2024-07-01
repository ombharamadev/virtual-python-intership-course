
### generte date from 1 may 2024 to 30 june 2024

from datetime import datetime , timedelta

start_date = datetime(2024,5,1)
end_date = datetime(2024,6,30)

while start_date < end_date:
    date = start_date.strftime("%Y-%m-%d")
    print(date)





    
    start_date = start_date + timedelta(days=1)