from datetime import datetime

# Get current date and time
now = datetime.now()

# Format the date and time
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Print the result
print("Current Date and Time:", formatted_date_time)