import time
import board
from adafruit_bme280 import basic as adafruit_bme280
from prometheus_client import start_http_server, Summary

temperature = Summary("temperature", "Temperature (C)")
humidity = Summary("humidity", "Humidity (%)")
pressure = Summary("pressure", "Pressure (hPa)")

i2c = board.I2C()

bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

if __name__ == "__main__":
    # Start up the server to expose the metrics.
    start_http_server(80)
    # Generate some requests.
    while True:
        temperature.observe(bme280.temperature)
        humidity.observe(bme280.relative_humidity)
        pressure.observe(bme280.pressure)
        time.sleep(2)
