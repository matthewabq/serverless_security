This folder contains a Python file written for Python 3.X that will allow sending in a bash commmand to run and spawn a subprocess that runs the command.  Also include are some test event files that can be utilized to test out your protected Lambda function by creating test events corresponding to the contents of the event files.

To protect this lambda function with Prisma Cloud Compute:
1. Create policy in Defend/Runtime/Serverless,
2. Create policy in Defend/Firewalls/CloudNativeAppFirewall/Serverless.
3. Download python based serverless defender as zip file here and unzip
4. Remove the comments for the 2 lines with 'twistlock' in main.py.
