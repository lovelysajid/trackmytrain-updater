import time
import random
from supabase import create_client, Client

SUPABASE_URL = "https://zbhkbroenqciwwholpmq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpiaGticm9lbnFjaXd3aG9scG1xIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTA5MTg3MTQsImV4cCI6MjEwNjQ5NDcxNH0.akzBOvTLTqtPgVl11yM2oLE20Oivu-SK9RTmFWAWbMA"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

TRAIN_ROUTES = {
    "1UP": {"name": "Khyber Mail", "route": [
        {"st": "Karachi Cantt", "lat": 24.8519, "lng": 67.0312},
        {"st": "Hyderabad Jn", "lat": 25.3960, "lng": 68.3578},
        {"st": "Rohri Junction", "lat": 27.6784, "lng": 68.8953},
        {"st": "Multan Cantt", "lat": 30.1978, "lng": 71.4697},
        {"st": "Lahore Junction", "lat": 31.5794, "lng": 74.3317},
        {"st": "Rawalpindi", "lat": 33.5970, "lng": 73.0479},
        {"st": "Peshawar Cantt", "lat": 34.0084, "lng": 71.5580}
    ]},
    "2DN": {"name": "Khyber Mail", "route": [
        {"st": "Peshawar Cantt", "lat": 34.0084, "lng": 71.5580},
        {"st": "Rawalpindi", "lat": 33.5970, "lng": 73.0479},
        {"st": "Lahore Junction", "lat": 31.5794, "lng": 74.3317},
        {"st": "Multan Cantt", "lat": 30.1978, "lng": 71.4697},
        {"st": "Rohri Junction", "lat": 27.6784, "lng": 68.8953},
        {"st": "Karachi Cantt", "lat": 24.8519, "lng": 67.0312}
    ]},
    "5UP": {"name": "Tezgam", "route": [
        {"st": "Karachi Cantt", "lat": 24.8519, "lng": 67.0312},
        {"st": "Hyderabad Jn", "lat": 25.3960, "lng": 68.3578},
        {"st": "Khanewal Jn", "lat": 30.3017, "lng": 71.9321},
        {"st": "Rawalpindi", "lat": 33.5970, "lng": 73.0479}
    ]},
    "7UP": {"name": "Tezraftar Express", "route": [
        {"st": "Karachi Cantt", "lat": 24.8519, "lng": 67.0312},
        {"st": "Multan Cantt", "lat": 30.1978, "lng": 71.4697},
        {"st": "Lahore Junction", "lat": 31.5794, "lng": 74.3317}
    ]},
    "10DN": {"name": "Allama Iqbal Express", "route": [
        {"st": "Sialkot Junction", "lat": 32.4945, "lng": 74.5229},
        {"st": "Lahore Junction", "lat": 31.5794, "lng": 74.3317},
        {"st": "Karachi Cantt", "lat": 24.8519, "lng": 67.0312}
    ]},
    "13UP": {"name": "Awam Express", "route": [
        {"st": "Karachi Cantt", "lat": 24.8519, "lng": 67.0312},
        {"st": "Rohri Junction", "lat": 27.6784, "lng": 68.8953},
        {"st": "Peshawar Cantt", "lat": 34.0084, "lng": 71.5580}
    ]},
    "14DN": {"name": "Awam Express", "route": [
        {"st": "Peshawar Cantt", "lat": 34.0084, "lng": 71.5580},
        {"st": "Rohri Junction", "lat": 27.6784, "lng": 68.8953},
        {"st": "Karachi Cantt", "lat": 24.8519, "lng": 67.0312}
    ]},
    "17UP": {"name": "Millat Express", "route": [
        {"st": "Karachi Cantt", "lat": 24.8519, "lng": 67.0312},
        {"st": "Faisalabad", "lat": 31.4187, "lng": 73.0791},
        {"st": "Lalamusa Junction", "lat": 32.7020, "lng": 73.9575}
    ]},
    "41UP": {"name": "Karakoram Express", "route": [
        {"st": "Karachi Cantt", "lat": 24.8519, "lng": 67.0312},
        {"st": "Faisalabad", "lat": 31.4187, "lng": 73.0791},
        {"st": "Lahore Junction", "lat": 31.5794, "lng": 74.3317}
    ]},
    "47UP": {"name": "Rehman Baba Express", "route": [
        {"st": "Karachi Cantt", "lat": 24.8519, "lng": 67.0312},
        {"st": "Multan Cantt", "lat": 30.1978, "lng": 71.4697},
        {"st": "Peshawar Cantt", "lat": 34.0084, "lng": 71.5580}
    ]}
}

def start_engine():
    print("🚀 TrackMyTrain Full Pakistan Railways Fleet Engine Active...")
    progress = {t_id: random.uniform(0.0, 0.8) for t_id in TRAIN_ROUTES.keys()}
    station_idx = {t_id: 0 for t_id in TRAIN_ROUTES.keys()}

    while True:
        for train_id, info in TRAIN_ROUTES.items():
            route = info["route"]
            curr_i = station_idx[train_id]
            next_i = (curr_i + 1) % len(route)

            start_node = route[curr_i]
            end_node = route[next_i]
            p = progress[train_id]

            lat = round(start_node["lat"] + (end_node["lat"] - start_node["lat"]) * p, 4)
            lng = round(start_node["lng"] + (end_node["lng"] - start_node["lng"]) * p, 4)
            speed = random.randint(68, 95)

            try:
                supabase.table("train_locations").upsert({
                    "train_id": train_id,
                    "train_name": info["name"],
                    "latitude": lat,
                    "longitude": lng,
                    "speed": speed,
                    "current_station": start_node["st"]
                }).execute()

                print(f"📡 [{train_id} - {info['name']}] {start_node['st']} -> Lat: {lat}, Lng: {lng} | {speed} km/h")
            except Exception as e:
                print(f"❌ Error [{train_id}]: {e}")

            progress[train_id] += 0.012
            if progress[train_id] >= 1.0:
                progress[train_id] = 0.0
                station_idx[train_id] = next_i

        print("-" * 65)
        time.sleep(2.5)

if __name__ == "__main__":
    start_engine()