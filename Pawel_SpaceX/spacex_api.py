import requests
import json

class RecordsAPI():
    BASE_URL = r"https://api.spacexdata.com/v3/launches/"

    def __init__(self, flight_number, mission_name, rocket_id, rocket_name, launch_date_utc, video_link):
        self.flight_number = flight_number
        self.mission_name = mission_name
        self.rocket_id = rocket_id
        self.rocket_name = rocket_name
        self.launch_date_utc = launch_date_utc
        self.video_link = video_link

    @classmethod
    def get_from_api(cls, flight_number):
        url = cls.BASE_URL + flight_number
        json_data = requests.get(url).json()
        return RecordsAPI(
            flight_number = flight_number,
            mission_name = json_data.get("mission_name"),
            rocket_id = json_data.get("rocket"),
            rocket_name = json_data.get("rocket"),
            launch_date_utc = json_data.get("launch_date_utc"),
            video_link = "video_link")
        
    @classmethod
    def get_results(cls):
        result = requests.get(cls.BASE_URL)
        result = result.json()
        return result

    @classmethod
    def get_flights_range(cls, show_max=False):
        url = cls.BASE_URL+"latest"
        json_data = requests.get(url).json()
        print(f"Last flight number: {json_data['flight_number']}") if show_max else None
        return json_data["flight_number"]

    @staticmethod
    def show_api():
        print(json.dumps(RecordsAPI.get_results(), sort_keys=True, indent=4))



class Flight(RecordsAPI):
    BASE_URL = r"https://api.spacexdata.com/v3/launches/"

    def __init__(self, flight_number, mission_name, rocket_id, rocket_name, launch_date_utc, video_link):
        self.flight_number = flight_number
        self.mission_name = mission_name
        self.rocket_id = rocket_id
        self.rocket_name = rocket_name
        self.launch_date_utc = launch_date_utc
        self.video_link = video_link
        
    @classmethod
    def create_by_flight_id(cls, flight_number):
        url = cls.BASE_URL + flight_number
        json_data = requests.get(url).json()
        flight = RecordsAPI.get_from_api(flight_number)
        return Flight(flight_number,
            json_data["mission_name"],
            json_data["rocket"]["rocket_id"], 
            json_data["rocket"]["rocket_name"], 
            json_data["launch_date_utc"], 
            json_data["links"]["video_link"])

    def show_info(self):
            print(f"""
            ------------ FLIGHT NUMBER {self.flight_number} -------------\n
            Mission name:\t {self.mission_name}\n
            Rocket ID: \t\t {self.rocket_id}\n
            Rocket Name: \t {self.rocket_name}\n
            Launch Date (UTC): \t {self.launch_date_utc}\n
            Video Link: \t {self.video_link}\n
            """)




# new_flight = Flight.create_by_flight_id("69")
# new_flight.show_info()
# RecordsAPI.get_flights_range()
# RecordsAPI.show_api()