from datetime import datetime
import pytz
import re
from tzlocal import get_localzone

# Mapping of common timezones to IANA timezone names
TIMEZONE_MAPPING = {
    'GMT': 'Iceland',
    'EAT': 'Indian/Mayotte',
    'CET': 'Indian/Mayotte',
    'WAT': 'Africa/Porto-Novo',
    'NST': 'Canada/Newfoundland',
    'AEDT': 'Australia/Victoria',
    'NZDT': 'Pacific/Auckland',
    'IST': 'Israel',
    'HKT': 'Hongkong',
    'WIB': 'Asia/Pontianak',
    'WIT': 'Asia/Jayapura',
    'PKT': 'Asia/Karachi',
    'WITA': 'Asia/Ujung_Pandang',
    'KST': 'ROK',
    'JST': 'Japan',
    'WET': 'WET',
    'ACDT': 'Australia/Yancowinna',
    'AEST': 'Australia/Queensland',
    'ACST': 'Australia/North',
    'AWST': 'Australia/West',
    'UTC': 'Zulu',
    'MSK': 'W-SU',
    'MET': 'MET',
    'ChST': 'Pacific/Saipan',
    'SST': 'US/Samoa',
    'EST': 'US/Eastern',
    'CST': 'US/Central',
    'MST': 'US/Mountain',
    'PST': 'US/Pacific',
    'AKST': 'US/Alaska',
    'HST': 'US/Hawaii',
    'AST': 'America/Anchorage',
    'PST': 'America/Los_Angeles',
    'MST': 'America/Denver',
    'CST': 'America/Chicago',
    'EST': 'America/New_York',
    'GMT': 'Europe/London'  # There was a missing closing parenthesis here

    # Add more mappings as needed
}

def convert_time(input_string):
    try:
        # Extract information from the input string using regex
        match = re.match(r'(\d{1,2}:\d{2}\s?[apAP]\.?[mM]\.?)\s+([A-Za-z\/_]+)\s+to\s+([A-Za-z\/_]+)', input_string)
        
        if match:
            input_time, input_timezone, output_timezone = match.groups()

            # Use the mapping or default to the input_timezone
            input_tz = pytz.timezone(TIMEZONE_MAPPING.get(input_timezone, input_timezone))

            # Parse the input time string
            input_time = datetime.strptime(input_time, '%I:%M %p')

            # Get the current date and time in the input time zone
            input_datetime = input_tz.localize(datetime.now().replace(hour=input_time.hour, minute=input_time.minute, second=0, microsecond=0))

            # Convert to the output time zone
            output_tz = pytz.timezone(TIMEZONE_MAPPING.get(output_timezone, output_timezone))
            output_time = input_datetime.astimezone(output_tz)

            # Format the converted time
            converted_time_str = output_time.strftime('%I:%M %p')

            return f"Converted time to {output_timezone}: {converted_time_str}"
        else:
            raise ValueError("Invalid input format. Please use the format: [time] [input timezone] to [output timezone]")
    except ValueError as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        input_string = input("Enter time conversion (e.g., 1:00 PM CST to PST): ")
        if input_string.lower() == 'exit':
            break
        result = convert_time(input_string)
        print(result)
