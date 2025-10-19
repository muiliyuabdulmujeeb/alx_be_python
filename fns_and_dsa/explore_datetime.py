from datetime import date, datetime, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date

current_date_time = display_current_datetime()
print(f"Current date and time: {current_date_time}")
number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(days):
    future_date = date.today() + timedelta(days= days)
    return future_date.strftime("%Y-%m-%d %H:%M:%S")

print(f"Future date is: {calculate_future_date(number_of_days)}")