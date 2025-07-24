from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Print the current date and time in its default format (YYYY-MM-DD HH:MM:SS.microseconds)
print("Current date and time:", current_datetime)

# You can also format the output string using strftime()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_datetime)