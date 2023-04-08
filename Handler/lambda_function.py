import boto3,json
import securityGroupPermission, newRelic, pingdom,newRelicthread, pingdomThread
import threading

#lamdahandler
def main(event, context):    
    #calling NewRelic Thread to sync new Relic Ips
    t1 = newRelicthread.PingdomThread()  
    
    #callingPingdom Thread to sync Pingdom Ips
    t2 = pingdomThread.NewRelicThread()
    
    t1.start()
    t2.start()
    try:
        t1.join()
        t2.join()
        return ('Ips updation successfull')
    
    #throw exception so that we can configure alert incase of failure to update
    except Exception as e:
        raise e
