import unittest
from gpiozero import LED
from beach import Beach
from beach_api import BeachAPI
from time import sleep

class TestBeach(unittest.TestCase):
    def setUp(self):
        api_client = BeachAPI()
        self.beach = Beach("Marselisborg Lystbådehavn, østmole", 56.1533, 10.2107, 0, 0, (17, 27), api_client)
        self.beach.set_led_pins((17,27))

    def test_set_LED_quality_status_1(self):
        self.beach.set_LED(1)
        sleep(4)

    def test_set_LED_quality_status_2(self):
        self.beach.set_LED(2)
        sleep(4)

    def test_set_LED_quality_status_other(self):
        self.beach.set_LED(3)
        sleep(4)

if __name__ == '__main__':
    unittest.main()