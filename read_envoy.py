import json
import requests
from requests.auth import HTTPDigestAuth


envoy_ip = 'ip'
envoy_user = 'envoy'
envoy_password = 'last6digitsofserial'
productionTableString = '/api/v1/production/inverters/' 
url = 'http://' + envoy_ip + productionTableString

def read_envoy_data(envoy_ip, envoy_user, envoy_password): 
    response = requests.get(url, auth=HTTPDigestAuth(envoy_user, envoy_password))     
    data = json.loads(response.text)
    return data

def main():
    data = read_envoy_data(envoy_ip, envoy_user, envoy_password)
    for item in data:
        print item['lastReportWatts']
main()
