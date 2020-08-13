import requests
import json
import uuid


class o365Endpoint:
    
    def __init__(self,o365Instance):
        self.sUUID = str(uuid.uuid4())
        self.instanceListURL = 'https://endpoints.office.com/version?ClientRequestId=' + self.sUUID
        self.o365Instance = o365Instance
        r = requests.get(self.instanceListURL)
        if (r.status_code == 200):
            o365InstanceDetails = json.loads(r.content.decode(r.encoding).replace("'",'"'))
            if next((item for item in o365InstanceDetails if item.get("instance") and item["instance"] == o365Instance), None) == None:
                self.instanceNames = []
                for instance in o365InstanceDetails:
                    for k, v in instance.items():
                        if (k == "instance"):
                            self.instanceNames.append(v)
                raise ValueError("FAILED: Valid instances are " + ', '.join(self.instanceNames) +".")
            else:
                self.endpointsURL = 'https://endpoints.office.com/endpoints/' + self.o365Instance + '?clientrequestid=' + self.sUUID
                self.updateJSON()
        else:
            print("Something went wrong")

        
    def listInstances(self):
        r = requests.get(self.instanceListURL)
        if (r.status_code == 200):
            o365InstanceDetails = json.loads(r.content.decode(r.encoding).replace("'",'"'))
            self.instanceNames = []
            for instance in o365InstanceDetails:
                for k, v in instance.items():
                    if (k == "instance"):
                        self.instanceNames.append(v)
            return self.instanceNames
        else:
            print("Something went wrong")

    def changeInstance(self, newInstance):
        r = requests.get(self.instanceListURL)
        if (r.status_code == 200):
            o365InstanceDetails = json.loads(r.content.decode(r.encoding).replace("'",'"'))
            if next((item for item in o365InstanceDetails if item.get("instance") and item["instance"] == newInstance), None) == None:
                self.instanceNames = []
                for instance in o365InstanceDetails:
                    for k, v in instance.items():
                        if (k == "instance"):
                            instanceNames.append(v)
                raise ValueError("FAILED: Valid instances are " + ', '.join(self.instanceNames) +".")
            else:
                self.o365Instance = newInstance
                self.endpointsURL = 'https://endpoints.office.com/endpoints/' + self.o365Instance + '?clientrequestid=' + self.sUUID
                self.updateJSON()
        else:
            print("Something went wrong")

    def updateJSON(self):
        print(self.endpointsURL)
        print(self.instanceListURL)
        r = requests.get(self.endpointsURL)
        if (r.status_code == 200):
            self.o365InstanceEndpoints = json.loads(r.content.decode(r.encoding).replace("'",'"'))
        else:
            print("Something went wrong")

# updateJSON()

#print("before __name__ guard")
if __name__ == '__main__':
    #print("Name was __main__")
    o365 = o365Endpoint('Worldwide')
    print(o365.o365Instance)
    #print(o365.o365InstanceEndpoints)
    o365.listInstances()

#print("after __name__ guard")