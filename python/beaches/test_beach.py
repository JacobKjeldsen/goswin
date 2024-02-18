import unittest
from gpiozero import LED
from beach import Beach

class TestBeach(unittest.TestCase):
    def setUp(self):
        self.beach = Beach()
        self.red_led = LED(1)
        self.green_led = LED(2)

    def test_set_LED_quality_status_1(self):
        self.beach.set_LED(1)
        self.assertTrue(self.red_led.is_active)
        self.assertFalse(self.green_led.is_active)

    def test_set_LED_quality_status_2(self):
        self.beach.set_LED(2)
        self.assertFalse(self.red_led.is_active)
        self.assertTrue(self.green_led.is_active)

    def test_set_LED_quality_status_other(self):
        self.beach.set_LED(3)
        self.assertFalse(self.red_led.is_active)
        self.assertFalse(self.green_led.is_active)

if __name__ == '__main__':
    unittest.main()