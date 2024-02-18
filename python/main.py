from beaches.beach import Beach
from beaches.beach_api import BeachAPI
import time

# led_groups = [ (23,24),(17,27),(22,10),(9,11), (19,26)]
# First group: (23,24) -> Den permanente
# Second group (17,27) -> Open Water
# Third group: (22,10) -> Havnebadet
# Fourth group (9,11) -> tangkrogen
# Fifth group (19,26) -> Marselisborg Badeklub
def make_beach_objects(api_client):
    beaches_json = api_client.get_beach_status()
    beach_objects = []
    denpermanente = Beach("Den Permanente", 56.1533, 10.2107, 0, 0, (23,24), api_client)
    havnebadet = Beach("Havnebadet Aarhus", 56.1555, 10.2107, 0, 0, (22,10), api_client)
    marselisborg = Beach("Marselisborg Lystbådehavn, østmole", 56.1533, 10.2107, 0, 0, (19,26), api_client)
    tangkrogen = Beach("Tangkrogen", 56.1533, 10.2107, 0, 0, (9,11), api_client)
    openwater = Beach("Open Water svømmebane", 56.1533, 10.2107, 0, 0, (17,27), api_client)
    beach_objects.append(denpermanente)
    beach_objects.append(havnebadet)
    beach_objects.append(marselisborg)
    beach_objects.append(tangkrogen)
    beach_objects.append(openwater)

    for beach in beach_objects:
        lat, longi = api_client.get_location(beaches_json, beach.get_name())
        beach.set_longitude(longi)
        beach.set_latitude(lat)
        temp, quality = api_client.get_status(beaches_json, beach.get_name())
        beach.set_water_temp(temp)
        beach.set_quality_status(quality)

    return beach_objects

def main():
    api_client = BeachAPI()
    beaches = make_beach_objects(api_client)
    while True:
        for beach in beaches:
            beaches_json = api_client.get_beach_status()
            temp, quality = api_client.get_status(beaches_json, beach.get_name())
            beach.set_water_temp(temp)
            beach.set_quality_status(quality)
        time.sleep(60*60*3) #3 hours


if __name__ == "__main__":
    main()