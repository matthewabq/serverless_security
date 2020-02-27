# ---------------------------------------------------------
# Author:  Matthew Barker, mbarker@paloaltonetworks.com
#
# To protect this lambda function with Prisma Cloud Compute:
#   - create policy in Defend/Runtime/Serverless
#   - create policy in Defend/Firewalls/CloudNativeAppFirewall/Serverless
#   - download python based serverless defender as zip file here and unzip
#   - remove the comments for the 2 lines with 'twistlock' in them
#   - zip up everything but the zip file (use -r option) and upload zip file to your new lambda function in AWS
# ----------------------------------------------------------

import subprocess
import os
import json
# import twistlock.serverless

# @twistlock.serverless.handler
def lambda_handler(event, context):
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
