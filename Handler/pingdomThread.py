import threading
import sys
import boto3,json
import securityGroupPermission, newRelic, pingdom

class PingdomThread(threading.Thread):
    def updatePingdomIp(self):
        session = boto3.Session()
        pingdomObj=pingdom.Pingdom()
        pingdomIps=pingdomObj.getIp()
        getAndUpdateSecurityGrp(session,"pingdom1",pingdomIps)
        
    def run(self):
        self.ex = None    
        try:
            self.updatePingdomIp()
        except BaseException as e:
            self.ex = e
   
    def join(self):
        threading.Thread.join(self)
        if self.ex:
            raise self.ex
            
def getAndUpdateSecurityGrp(session,sgname,probeIp):
    regions=["us-east-1","us-west-1","eu-west-1","eu-central-1","ap-southeast-2"]
    for reg in regions:
        ec2Resource = session.resource("ec2", region_name=reg)
        groups = ec2Resource.security_groups.filter(Filters=[{"Name": "group-name", "Values": [sgname]}])
        for grp in groups:
            securityGroup=securityGroupPermission.SecurityGroupPermission(grp.id,ec2Resource)
            securityGroup.compareAndUpdateIps(probeIp,sgname)
