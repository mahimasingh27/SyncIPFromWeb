import requests;
import json;

class NewRelic:
    def __init__(self):
        self.URL="https://s3.amazonaws.com/nr-synthetics-assets/nat-ip-dnsname/production/ip-ranges.json"
    
    def getIp(self):
        newrelicResponse=requests.get(self.URL)
        newRelicIp=set()
        NrResponseContent = json.loads(newrelicResponse.content)
        for iterator in NrResponseContent:
            for ipAddress in NrResponseContent[iterator]:
                newRelicIp.add(ipAddress)
        return newRelicIp
