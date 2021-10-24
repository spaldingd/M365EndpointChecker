#! /user/bin/env python
"""
A module to help identifying Microsoft 365 endpoints utilising the endpoints JSON file provided by Microsoft.

https://docs.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-endpoints?view=o365-worldwide
"""

import requests
import json
import uuid


class O365Endpoint:
    
    def __init__(self, instance):
        self.sUUID = str(uuid.uuid4())
        self.instanceListURL = 'https://endpoints.office.com/version?ClientRequestId={}'.format(self.sUUID)
        self.instance = instance
        r = requests.get(self.instanceListURL)
        if r.status_code == 200:
            o365instancedetails = json.loads(r.content.decode(r.encoding).replace("'", '"'))
            if next((item for item in o365instancedetails if item.get("instance") and item["instance"] == instance)
                    , None) is None:
                self.instanceNames = []
                for instance in o365instancedetails:
                    for k, v in instance.items():
                        if k == "instance":
                            self.instanceNames.append(v)
                raise ValueError("FAILED: Valid instances are " + ', '.join(self.instanceNames) + ".")
            else:
                self.endpointsURL = 'https://endpoints.office.com/endpoints/{}?clientrequestid={}'.format(self.instance
                                                                                                          , self.sUUID)
                self.updatejson()
        else:
            print("Something went wrong")

    def listinstances(self):
        r = requests.get(self.instanceListURL)
        if r.status_code == 200:
            o365instancedetails = json.loads(r.content.decode(r.encoding).replace("'", '"'))
            self.instanceNames = []
            for instance in o365instancedetails:
                for k, v in instance.items():
                    if k == "instance":
                        self.instanceNames.append(v)
            return self.instanceNames
        else:
            print("Something went wrong")

    def changeinstance(self, newinstance):
        r = requests.get(self.instanceListURL)
        if r.status_code == 200:
            o365instancedetails = json.loads(r.content.decode(r.encoding).replace("'", '"'))
            if next((item for item in o365instancedetails if item.get("instance") and item["instance"] == newInstance)
                    , None) is None:
                self.instanceNames = []
                for instance in o365instancedetails:
                    for k, v in instance.items():
                        if k == "instance":
                            instanceNames.append(v)
                raise ValueError("FAILED: Valid instances are " + ', '.join(self.instanceNames) + ".")
            else:
                self.instance = newinstance
                self.endpointsURL = 'https://endpoints.office.com/endpoints/{}?clientrequestid={}'.format(self.instance
                                                                                                          , self.sUUID)
                self.updateJSON()
        else:
            print("Something went wrong")

    def updatejson(self):
        r = requests.get(self.endpointsURL)
        if r.status_code == 200:
            self.rawjson = json.loads(r.content.decode(r.encoding).replace("'", '"'))
        else:
            print("Something went wrong")


if __name__ == '__main__':
    o365 = O365Endpoint('Worldwide')
    print(o365.instance)
    o365.listinstances()
    print(o365.rawjson)