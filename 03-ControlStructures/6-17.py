time=input("Enter time (24-hour format): ")


# Split the input into hours and minutes
hours, minutes = map(int, time.split(':'))

if hours >=12:
    period="pm"
    if hours>12:
        hours=-12
else:
    period="am"
    if hours==0:
        hours=12

print(f"Time in 12-hour format: {hours}:{minutes:02d}{period}")


       
