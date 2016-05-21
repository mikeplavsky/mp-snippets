from __future__ import print_function

import json
import urlparse
import os

import boto3
db = boto3.resource("dynamodb")

t = db.Table("aws-command")

print('Loading function')

def lambda_handler(event, context):
    
    cmd = urlparse.parse_qs(
            event["body"])
    
    res = json.dumps(cmd)
    print(res)
    
    print(
        context.aws_request_id)
        
    text = "help"
    
    if cmd.has_key("text"):
        text = cmd["text"][0]
        
    t.put_item(
        Item = dict(
            RequestId = context.aws_request_id,
            response_url = cmd["response_url"][0],
            user = cmd["user_name"][0],
            command = cmd["command"][0],
            text = text))
    
    return dict(
        response_type = "in_channel",
        text = "Yep!",
        attachments = [
                  dict(
                    text = "Got it, %s!" % cmd["user_name"][0],
                    color = "good")])
                
                
