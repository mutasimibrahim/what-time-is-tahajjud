import json
from requestPrayerTime import result
from datetime import date

# The variable "result" is the api response.
api_response = result

# Parse the JSON response
response_data = api_response.get('data', [])

# Today's date
target_date = date.today()
formatted_date = target_date.strftime('%d-%m-%Y')

# Iterate through data array to find formatted_date
prayer_times = None
for entry in response_data:
    if entry['date']['gregorian']['date'] == formatted_date:
        prayer_times = entry['timings']
        break

# Print the extracted prayer times
if prayer_times:
    print(f"Prayer times for {target_date}")
    for prayer, time in prayer_times.items():
        print(f"{prayer}: {time}")

else:
    print(f"No data found for {target_date}")


# Print when the last third of the nigth begins
tahajjud_time = None
for entry in response_data:
    if entry['date']['gregorian']['date'] == formatted_date:
        tahajjud_time = entry['timings']['Lastthird']
        break

if tahajjud_time is not None:
  print("The last third of the night is from: " + str(tahajjud_time) + " to: " + entry['timings']['Fajr'])
else:
  print("No data found for the last third of the night.")