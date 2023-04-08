import boto3,json
import securityGroupPermission, newRelic, pingdom,newRelicthread, pingdomThread
import threading

#lamdahandler
def main(event, context):    
    
    t1 = newRelicthread.PingdomThread()   
    t2 = pingdomThread.NewRelicThread()
    t1.start()
    t2.start()
    try:
        t1.join()
        t2.join()
        return ('Ips updation successfull')

    except Exception as e:
        raise e
