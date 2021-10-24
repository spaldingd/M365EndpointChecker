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
        self.raw_json = ""
        r = requests.get(self.instanceListURL)
        if r.status_code == 200:
            m_365_instance_details = json.loads(r.content.decode(r.encoding).replace("'", '"'))
            if next((item for item in m_365_instance_details if item.get("instance") and item["instance"] == instance)
                    , None) is None:
                self.instance_names = []
                for instance in m_365_instance_details:
                    for k, v in instance.items():
                        if k == "instance":
                            self.instance_names.append(v)
                raise ValueError("FAILED: Valid instances are " + ', '.join(self.instance_names) + ".")
            else:
                self.endpointsURL = 'https://endpoints.office.com/endpoints/{}?clientrequestid={}'.format(self.instance
                                                                                                          , self.sUUID)
                self.update_json()
        else:
            print("Something went wrong")

    def list_instances(self):
        r = requests.get(self.instanceListURL)
        if r.status_code == 200:
            m_365_instance_details = json.loads(r.content.decode(r.encoding).replace("'", '"'))
            self.instance_names = []
            for instance in m_365_instance_details:
                for k, v in instance.items():
                    if k == "instance":
                        self.instance_names.append(v)
            return self.instance_names
        else:
            print("Something went wrong")

    def change_instance(self, new_instance):
        r = requests.get(self.instanceListURL)
        if r.status_code == 200:
            m_365_instance_details = json.loads(r.content.decode(r.encoding).replace("'", '"'))
            if next((item for item in m_365_instance_details if item.get("instance") and item["instance"] == new_instance), None) is None:
                self.instance_names = []
                for instance in m_365_instance_details:
                    for k, v in instance.items():
                        if k == "instance":
                            self.instance_names.append(v)
                raise ValueError("FAILED: Valid instances are " + ', '.join(self.instance_names) + ".")
            else:
                self.instance = new_instance
                self.endpointsURL = 'https://endpoints.office.com/endpoints/{}?clientrequestid={}'.format(self.instance
                                                                                                          , self.sUUID)
                self.update_json()
        else:
            print("Something went wrong")

    def update_json(self):
        r = requests.get(self.endpointsURL)
        if r.status_code == 200:
            self.raw_json = json.loads(r.content.decode(r.encoding).replace("'", '"'))
        else:
            print("Something went wrong")


if __name__ == '__main__':
    o365 = O365Endpoint('Worldwide')
    print(o365.instance)
    o365.list_instances()
    print(o365.raw_json)
