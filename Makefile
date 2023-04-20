venv:
	python3 -m venv .venv

requirements:
	.venv/bin/pip install -r requirements.txt

freeze:
	.venv/bin/pip freeze > requirements.txt

install: venv requirements
	envsubst < sensor-exporter.service > /etc/systemd/system/sensor-exporter.service
	systemctl start sensor-exporter
	systemctl enable sensor-exporter
