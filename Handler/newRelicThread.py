import threading
import sys
import boto3,json
import securityGroupPermission, newRelic, pingdom, pingdomThread

class NewRelicThread(threading.Thread):
   
    def updateNewRelicIp(self):
        session = boto3.Session()
        newRelicObj=newRelic.NewRelic()
        newRelicIps= newRelicObj.getIp()
        getAndUpdateSecurityGrp(session,"newrelic_synthetic",newRelicIps)

    def run(self):
        self.ex = None    
        try:
            self.updateNewRelicIp()
        except BaseException as e:
            self.ex = e
   
    def join(self):
        threading.Thread.join(self)
        if self.ex:
            raise self.ex
