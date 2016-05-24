from __future__ import print_function

import urllib
import urllib2
import boto3

ec2 = boto3.resource("ec2")

import json
print('Loading function')

def call(url, params=dict()):
    
    data = json.dumps(
        params)
    
    req = urllib2.Request(
        url,
        data,
        headers={
            "content-type":"application/json"})
    
    return urllib2.urlopen(req)
    

def lambda_handler(event, context):
    
    r = event["Records"][0]
    
    if r["eventName"] != "INSERT":
        return "Not Insert"
    
    print(
        json.dumps(r))
        
    url = r["dynamodb"]["NewImage"]["response_url"]["S"]
    print(url)
    
    i = [x for x in ec2.instances.all()]
    print(len(i))    
    
    res = call(
        url,
        dict(
            text="Yep, Done!",
            attachments=[
                dict(text="All: %s" % len(i))]))
        
    print(
        res.read())
        
    return "Done"
   
