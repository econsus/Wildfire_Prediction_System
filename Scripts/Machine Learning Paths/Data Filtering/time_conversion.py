import pandas as pd

def convert_time(year, month, day, hour):
    # Convert all arguments to integers
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)

    # Convert the hour to a string
    hour_str = str(hour)

    # Pad the string with zeros to ensure it has at least four digits
    hour_str_padded = hour_str.zfill(4)

    # Extract hours
    hours = int(hour_str_padded[:2])

    # Create a datetime object using the provided year, month, day, and hours
    dt = pd.to_datetime(f'{year}-{month}-{day} {hours}:00')

    # Convert the datetime object to a string in the "Year/month/day time" format
    formatted_time = dt.strftime('%Y/%m/%d %H:%M')

    return formatted_time

# Example usage
if __name__ == "__main__":
    year = 2019.3
    month = 1.2
    day = 1.15
    hour = 56.789

    formatted_time = convert_time(year, month, day, hour)
    print(formatted_time)
