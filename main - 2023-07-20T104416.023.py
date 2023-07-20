import requests
import json
import time

def get_flight_data(api_key):
    base_url = 'https://api.exampleflighttracker.com/v1/flights'
    
    # Get current timestamp to filter flights only in the last 24 hours
    current_time = int(time.time())
    one_day_ago = current_time - (24 * 60 * 60)
    
    # API parameters for querying flights taking off and landing
    params = {
        'api_key': api_key,
        'begin': one_day_ago,
        'end': current_time,
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error: Failed to fetch flight data.")
        return None

def main():
    # Replace 'YOUR_API_KEY' with your actual flight tracking API key
    api_key = 'YOUR_API_KEY'
    
    flight_data = get_flight_data(api_key)
    
    if flight_data:
        for flight in flight_data['flights']:
            flight_number = flight['flight_number']
            departure = flight['departure']
            arrival = flight['arrival']
            status = flight['status']
            
            print(f"Flight {flight_number} - {status}")
            print(f"Departure: {departure['airport']} ({departure['iata']}) at {departure['time']}")
            print(f"Arrival: {arrival['airport']} ({arrival['iata']}) at {arrival['time']}\n")

if __name__ == "__main__":
    main()

