from beaches.beach import Beach
from beaches.beach_api import BeachAPI
import time


def make_beach_objects(api_client):
    beaches_json = api_client.get_beach_status()
    beach_objects = []
    #denpermanente = Beach("Den Permanente", 56.1533, 10.2107, 0, 0, (0, 0), api_client)
    #havnebadet = Beach("Havnebadet Aarhus", 56.1555, 10.2107, 0, 0, (0, 0), api_client)
    marselisborg = Beach("Marselisborg Lystbådehavn, østmole", 56.1533, 10.2107, 0, 0, (17, 27), api_client)
    #tangkrogen = Beach("Tangkrogen", 56.1533, 10.2107, 0, 0, (0, 0), api_client)
    #openwater = Beach("Open Water svømmebane", 56.1533, 10.2107, 0, 0, (0, 0), api_client)
    #beach_objects.append(denpermanente)
    #beach_objects.append(havnebadet)
    beach_objects.append(marselisborg)
    #beach_objects.append(tangkrogen)
    #beach_objects.append(openwater)

    for beach in beach_objects:
        lat, long = api_client.get_location(beaches_json, beach.get_name())
        beach.set_longitude(long)
        beach.set_latitude(lat)
        temp, quality = api_client.get_status(beaches_json, beach.get_name())
        beach.set_water_temp(temp)
        beach.set_quality_status(quality)

    return beach_objects

def main():
    api_client = BeachAPI()
    beaches = make_beach_objects(api_client)
    # Check for new beach status every 5 minutes
    while True:
        for beach in beaches:
            beaches_json = api_client.get_beach_status()
            temp, quality = api_client.get_status(beaches_json, beach.get_name())
            beach.set_water_temp(temp)
            beach.set_quality_status(quality)
        time.sleep(300)


def test():
    api_client = BeachAPI()
    status = api_client.get_beach_status()
    
    print(api_client.get_status(status, "Den Permanente"))

if __name__ == "__main__":
    main()