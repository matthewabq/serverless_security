import subprocess
import os
import json

# add these next three lines for Prisma Cloud Compute python protection
# import twistlock.serverless
#
# @twistlock.serverless.handler
def handler(event, context):
    cmd = "echo Hello world"
    if "cmd" in event:
        cmd = event["cmd"]

    try:
        result =  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout
        out =  result.read()
        out = out.decode("utf8")
    except Exception as e:
        out = str(e)

    response = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": out
    }

    return response
