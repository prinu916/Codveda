import requests
API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """Fetch and display weather data for a given city."""
    try:
    
        url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
        
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            print("\n🌍 Weather Information:")
            print(f"City: {data['name']}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Weather: {data['weather'][0]['description'].title()}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        elif response.status_code == 404:
            print("⚠️ City not found. Please check the name and try again.")
        else:
            print(f"⚠️ Error: Unable to fetch data (Status Code: {response.status_code})")

    except requests.exceptions.RequestException as e:
        print("❌ Network error occurred:", e)


def main():
    print("=== WEATHER API INTEGRATION ===")
    city = input("Enter city name: ").strip()
    if city:
        get_weather(city)
    else:
        print("⚠️ City name cannot be empty!")

if __name__ == "__main__":
    main()
