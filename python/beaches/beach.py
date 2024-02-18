import gpiozero

# Defines a class, Beach, representing a beach gps location, current water temperature and quality status. Should also define a pointer of a set of two LED GPIO pins to be used for the beach's status LED.
class Beach:
    def __init__(self, name, longitude, latitude, water_temp, quality_status, led_pins, api_client):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.water_temp = water_temp
        self.quality_status = quality_status
        # (red, green) e.g. (17, 18)
        self.led_pins = led_pins
        self.api_client = api_client

    def get_name(self):
        return self.name
    
    def get_longitude(self):
        return self.longitude
    
    def get_latitude(self):
        return self.latitude

    def get_water_temp(self):
        return self.water_temp

    def get_quality_status(self):
        return self.quality_status

    def get_led_pins(self):
        return self.led_pins
    
    def set_name(self, name):
        self.name = name

    def set_longitude(self, longitude):
        self.longitude = longitude
    
    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_water_temp(self, water_temp):
        self.water_temp = water_temp

    def set_quality_status(self, quality_status):
        self.quality_status = quality_status
        self.set_LED(quality_status)

    def set_led_pins(self, led_pins):
        self.led_pins = led_pins

    # Quality status: 1 = bad (red LED), 2 = good (green LED)
    def set_LED(self, quality_status):
        red_led = gpiozero.LED(self.led_pins[0])
        green_led = gpiozero.LED(self.led_pins[1])
        if quality_status == 1:
            red_led.on()
            green_led.off()
        elif quality_status == 2:
            red_led.off()
            green_led.on()
        else:
            red_led.off()
            green_led.off()
        
