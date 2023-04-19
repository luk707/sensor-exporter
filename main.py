import time
import board
from adafruit_bme280 import basic as adafruit_bme280
import adafruit_veml7700


i2c = board.I2C()

bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
veml7700 = adafruit_veml7700.VEML7700(i2c)

while True:
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.relative_humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Ambient light:", veml7700.light)
    print("Lux:", veml7700.lux)
    time.sleep(2)
