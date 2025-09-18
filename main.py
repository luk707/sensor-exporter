import time
import socket
import board
from adafruit_bme280 import basic as adafruit_bme280
from prometheus_client import start_http_server, Summary

# Get the hostname of the machine
HOSTNAME = socket.gethostname()

# Define metrics with a 'hostname' label
temperature = Summary("temperature", "Temperature (C)", ["hostname"])
humidity = Summary("humidity", "Humidity (%)", ["hostname"])
pressure = Summary("pressure", "Pressure (hPa)", ["hostname"])


def main():
    # Initialize I2C and sensor
    i2c = board.I2C()
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, 0x76)

    # Start up the server to expose the metrics.
    start_http_server(80)

    # Continuously collect and expose sensor data
    while True:
        temperature.labels(HOSTNAME).observe(bme280.temperature)
        humidity.labels(HOSTNAME).observe(bme280.relative_humidity)
        pressure.labels(HOSTNAME).observe(bme280.pressure)
        time.sleep(2)


if __name__ == "__main__":
    main()
