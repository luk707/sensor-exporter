import time
import board
from adafruit_bme280 import basic as adafruit_bme280
import adafruit_veml7700
from adafruit_seesaw.seesaw import Seesaw
from prometheus_client import start_http_server, Summary

moisture = Summary('moisture', 'Moisture')
temperature = Summary('temperature', 'Temperature (C)')
humidity = Summary('humidity', 'Humidity (%)')
pressure = Summary('pressure', 'Pressure (hPa)')
light = Summary('light', 'Light')
lux = Summary('lux', 'Light (lux)')

i2c = board.I2C()

bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
veml7700 = adafruit_veml7700.VEML7700(i2c)
ss = Seesaw(i2c, addr=0x36)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(80)
    # Generate some requests.
    while True:
        moisture.observe(ss.moisture_read())
        temperature.observe(bme280.temperature)
        humidity.observe(bme280.relative_humidity)
        pressure.observe(bme280.pressure)
        light.observe(veml7700.light)
        lux.observe(veml7700.lux)
        time.sleep(2)
