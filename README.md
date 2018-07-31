# enphase2influx

Dumps locally available Envoy-S metering data from http://local_enphase/production.json and put those data in InfluxDB for graphing using Grafana. Scripts provided to read the data every 15 seconds, works well on a PI. Does not rely on Enphase distant API (hence no cloud API or cloud server).

Requires:
- influxdb installed with a database called enphase
- Enphase Envoy-S with a known IP address

Installation:
- Tests can be locally done using the `pullAndSend.py` script
- Automatic mode can be done using the script `enphase2Influx_15sec.sh` which will dump the data every 15 seconds to the DB (which is quite a lot)
- The `enphase.service`, which is `systemd` unit file, can be used for startup at login in Linux
