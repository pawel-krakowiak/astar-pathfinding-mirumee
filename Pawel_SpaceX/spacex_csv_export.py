from objects_flight_create import objects, create_all_flights
import logging
import csv

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

def exportToFile_Static(path, header, data):
    with open(path, mode="a") as file:
        items_list = [header+"\t:\t"+data]
        writer = csv.writer(file)
        
        if header == "obj.flight_number":
            writer.writerow([]*2)

        for item in items_list:
            writer.writerow([item])
    

headers_pro = ["obj.flight_number", "obj.mission_name", "obj.rocket_id", "obj.rocket_name", "obj.launch_date_utc", "obj.video_link"]
objects = create_all_flights()

for obj in objects:
    for attr in headers_pro:
        exportToFile_Static(r"Pawel_SpaceX\CSV_data\objects.csv", attr, eval(attr))
        # eval("print("+attr+"\n)")
 
    