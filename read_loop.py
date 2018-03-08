import json
import requests
import time
from influxdb import InfluxDBClient

envoy_ip = 'ip'
envoy_user = 'envoy'
envoy_password = 'last6digitsofserial'
url = 'http://' + envoy_ip + '/production.json'

def startLoop():
    try:
        response = requests.get(url, timeout=4)
        data = json.loads(response.text)
        client = InfluxDBClient('ip', 8086, 'user', 'pass', 'database_name')
        InstantConsumption = data['consumption'][0]['wNow']
        InstantGeneration = data['production'][1]['wNow']
        GenerationToday = data['production'][1]['whToday']
        GridUsage = data['consumption'][1]['wNow']
        ConsumptionToday = data['consumption'][0]['whToday']
        LifetimeGeneration = data['production'][1]['whLifetime']
        LifetimeConsumption = data['consumption'][0]['whLifetime']
        LifetimeGridConsumption = data['consumption'][1]['whLifetime']
        json_body = [
        {
            "measurement": "solar",
            "tags": {
                "host": "envoy"
            },
            "fields": {
                "InstantConsumption": InstantConsumption,
                "InstantGeneration": InstantGeneration,
                "GridUsage": GridUsage,
                "GenerationToday": GenerationToday,
                "ConsumptionToday": ConsumptionToday,
                "LifetimeGeneration": LifetimeGeneration,
                "LifetimeConsumption": LifetimeConsumption,
                "LifetimeGridConsumption": LifetimeGridConsumption
            }
        }
        ]
        
        client.write_points(json_body)
    except:
        pass
    

    time.sleep(5)
    
while True:
    startLoop()
