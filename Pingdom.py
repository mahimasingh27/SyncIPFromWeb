import requests;

class Pingdom:
    def __init__(self):
        self.URL="https://my.pingdom.com/probes/ipv4"
    def getPingdomProbeIp(self):
        pingdomResponse=requests.get(self.URL)
        temp=set(pingdomResponse.text.strip().split("\n"))
        pingdomIps= set(map(lambda x: x+"/32", temp))
        return pingdomIps
    
