import random
import time
import json

# --- CONFIGURATION ---
#### This is a66666 placeholder key for testing your push capabilities.
#### In a real scenario, use environment variables!
API_KEY = "sk-test-51MzW2E2e9df90123-REDACTED-RANDOM-KEY-99"
BASE_URL = "https://api.mockweather.io/v1/"

class WeatherTester:
    """A class to simulate2 data processing for a GitHub push test 2."""
    
    def __init__(self, location):
        self.location = location
        self.data_log = []

    def fetch_mock_data(self):
        """Simulates fetching weather data using the API key."""
        print(f"Connecting to {BASE_URL} with key: {API_KEY[:8]}...")
        # Simulate a network delay
        time.sleep(0.1)
        
        return {
            "temp": round(random.uniform(-10, 40), 2),
            "humidity": random.randint(30, 90),
            "condition": random.choice(["Sunny", "Cloudy", "Rainy", "Snowy"]),
            "timestamp": time.time()
        }

    def run_simulation(self, iterations=15):
        """Generates multiple entries to increase file complexity."""
        print(f"Starting simulation for: {self.location}")
        for i in range(iterations):
            record = self.fetch_mock_data()
            self.data_log.append(record)
            print(f"Iteration {i+1}: Recorded {record['temp']}°C")
            
    def save_results(self):
        filename = f"{self.location.lower()}_results.json"
        with open(filename, 'w') as f:
            json.dump(self.data_log, f, indent=4)
        print(f"Results saved to {filename}")

def main():
    # Adding extra boilerplate to ensure we hit the 100-line mark
    locations = ["New York", "London", "Tokyo", "Sydney", "Berlin"]
    
    print("--- GIT PUSH TEST SCRIPT START ---")
    
    # Logic flow to demonstrate a 'real' application structure
    for city in locations:
        tester = WeatherTester(city)
        tester.run_simulation(iterations=5)
        tester.save_results()
        
    print("\nProcessing complete. Check the generated JSON files.")
    print("If you see this code in your repo, your push was successful.")

# Extra padding to reach 100 lines for your file size requirement
# ------------------------------------------------------------
# Padding line 65
# Padding line 66
# Padding line 67
# Padding line 68
# Padding line 69
# Padding line 70
# Padding line 71
# Padding line 72
# Padding line 73
# Padding line 74
# Padding line 75
# Padding line 76
# Padding line 77
# Padding line 78
# Padding line 79
# Padding line 80
# Padding line 81
# Padding line 82
# Padding line 83
# Padding line 84
# Padding line 85
# Padding line 86
# Padding line 87
# Padding line 88
# Padding line 89
# Padding line 90
# Padding line 91
# Padding line 92
# Padding line 93
# Padding line 94
# Padding line 95
# Padding line 96

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred during testing: {e}")

# End of line 100
