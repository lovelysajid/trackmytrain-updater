
import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {
    "User-Agent": "okhttp/4.12.0",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

BASE_URL = "https://app-api.pakraillive.com/api"

# Query parameter tests
TEST_PARAMS = [
    {"TrainId": 6},
    {"trainId": 6},
    {"train_id": 6},
    {"TrainId": "6DN"},
    {"trainId": "6DN"}
]

print("🎯 Testing Query Parameters on Working Endpoint...")

for params in TEST_PARAMS:
    url = f"{BASE_URL}/Train/GetTrainStationsByTrainId"
    try:
        res = requests.get(url, headers=HEADERS, params=params, timeout=5, verify=False)
        print(f"GET {url} Params: {params} -> Status: {res.status_code}")
        data = res.json()
        if data.get("IsSuccess") and len(data.get("Response", [])) > 0:
            print("🎉 GOT REAL TRAIN DATA!")
            print(json.dumps(data, indent=2)[:500])
            break
        else:
            print(f"Response: {data}")
    except Exception as e:
        print(f"Error: {e}")

print("-" * 50)