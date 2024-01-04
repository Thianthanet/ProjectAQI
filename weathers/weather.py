import requests
import csv
from datetime import datetime
import time

# API endpoint
api_url = "http://api.airvisual.com/v2/city"
api_key = "7e175a5b-f000-4f22-bd75-8757dd1c94b3"

# Specify city, state, and country
city = "Yangon"
state = "Yangon"
country = "Myanmar"

# Construct the API request URL
api_request_url = f"{api_url}?city={city}&state={state}&country={country}&key={api_key}"

# Set the interval for fetching data (in seconds)
fetch_interval = 3600  # 1 hour

try:
    while True:
        # Make the API request
        response = requests.get(api_request_url)
        data = response.json()

        # Extract relevant information
        aqi = data['data']['current']['pollution']['aqius']
        date = datetime.now().strftime("%Y-%m-%d")
        time_now = datetime.now().strftime("%H:%M:%S")

        # Print the obtained information
        print(f"AQI: {aqi}")
        print(f"Date: {date}")
        print(f"Time: {time_now}")

        # Save the data to a CSV file
        csv_filename = "air_quality_data.csv"
        with open(csv_filename, mode='a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            # Write header if the file is empty
            if csv_file.tell() == 0:
                csv_writer.writerow(["AQI", "Date", "Time"])
            csv_writer.writerow([aqi, date, time_now])

        print(f"Data saved to {csv_filename}")

        # Wait for the next interval before making the next API request
        time.sleep(fetch_interval)

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from the API: {e}")
except KeyboardInterrupt:
    print("Data fetching stopped.")
