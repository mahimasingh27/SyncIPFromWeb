import boto3,json
import securityGroupPermission, newRelic, pingdom,threadClass
import threading

#lamdahandler
def main(event, context):    
    
    t1 = threadClass.PingdomThread()   
    t2 = threadClass.NewRelicThread()
    t1.start()
    t2.start()
    try:
        t1.join()
        t2.join()
        return ('Ips updation successfull')

    except Exception as e:
        raise e
