# enphase2influx

Dumps locally available Envoy-S metering data from http://local_enphase/production.json and put those data in InfluxDB for graphing using Grafana. Scripts provided to read the data every 15 seconds, works well on a PI. Does not rely on Enphase distant API (hence no cloud API or cloud server).
