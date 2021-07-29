#!/usr/bin/env python3

from pyaim import CCPPasswordRESTSecure

aimccp = CCPPasswordRESTSecure('https://cyberark.dvdangelo33.dev/', "clientcert.pem", verify=True)
r = aimccp.GetPassword(appid='pyAIM',safe='D-AWS-AccessKeys',username='AnsibleAWSUser')
print(r)
