from datetime import datetime,date,timedelta
current_date = datetime.now()
def display_current_datetime():
    print(f"Current date and time: {current_date.replace(microsecond=0)}")
display_current_datetime()

def calculate_future_date():
    number_of_days  = int(input("Enter the number of days to add to the current date: "))
    delta_time = timedelta(days=number_of_days)
    future_date = current_date.date() + delta_time
    print(f"Future date: {future_date}")
calculate_future_date()
