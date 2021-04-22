from spacex_api import Flight, RecordsAPI
import logging

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

def create_all_flights():
    object_list = []

    for flight_id in range(1, RecordsAPI.get_flights_range()):
        new_flight = Flight.create_by_flight_id(str(flight_id))
        object_list.append(new_flight)
        logging.info("Object ID: %d created", flight_id)
    print(f"Objects created: {len(object_list)}")
    return object_list

def show_all_obj_info(objects):
    for obj in objects:
        print(obj.show_info())

objects = []

# objects = create_all_flights()
# show_all_obj_info(objects)





