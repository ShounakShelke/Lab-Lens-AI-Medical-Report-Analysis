import requests
import os

url = 'http://localhost:5000/api/analyze'
files = {'file': open('../report_high_risk.png', 'rb')}

try:
    r = requests.post(url, files=files)
    print(r.status_code)
    print("FULL RESPONSE:")
    print(r.json())
except Exception as e:
    print(f"Error: {e}")
