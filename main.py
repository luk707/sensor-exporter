import time
import socket

# import board
from bmp280 import BMP280
from prometheus_client import start_http_server, Summary

# Get the hostname of the machine
HOSTNAME = socket.gethostname()

# Define metrics with a 'hostname' label
temperature = Summary("temperature", "Temperature (C)", ["hostname"])
humidity = Summary("humidity", "Humidity (%)", ["hostname"])
pressure = Summary("pressure", "Pressure (hPa)", ["hostname"])


def main():
    # Initialize sensor
    bmp280 = BMP280(0x76)

    # Start up the server to expose the metrics.
    start_http_server(80)

    # Continuously collect and expose sensor data
    while True:
        temperature.labels(HOSTNAME).observe(bmp280.get_temperature())
        pressure.labels(HOSTNAME).observe(bmp280.get_pressure())
        time.sleep(2)


if __name__ == "__main__":
    main()
