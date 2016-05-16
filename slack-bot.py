from __future__ import print_function

import urllib2
import urllib
import json

token = "<TOKEN>"

def call(meth, params=dict()):
    
    values = dict(
        token = token
        )
        
    values.update(params)
        
    data = urllib.urlencode(
        values)
    
    req = urllib2.Request(
        "https://slack.com/api/%s" % meth,
        data)
    
    raw = urllib2.urlopen(req)
    
    return json.loads(
        raw.read())


def lambda_handler(event, context):

    res = call("im.list")
    
    for im in res["ims"]:
        
        print(im)
        
        res = call(
            "im.history",
            dict(channel=im["id"]))
            
        print(len(res["messages"]))
            
        if len(res["messages"]):
            
            m = res["messages"][0]
            print(m["text"])
            
            if m["user"] == "U18UVBHAB":
                continue
            
            res = call(
                "chat.postMessage",
                dict(
                    text = "Got it! ",
                    channel = im["id"],
                    as_user=True))
                
            print(res)
            
    return "Done" 
