import requests
import json
import uuid


class o365Endpoint:
    
    def __init__(self,o365Instance):
        self.instanceListURL = 'https://endpoints.office.com/version?ClientRequestId=' + str(uuid.uuid4())
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
                self.endpointsURL = 'https://endpoints.office.com/endpoints/' + self.o365Instance + '?clientrequestid=' + str(uuid.uuid4())
        else:
            print("Something went wrong")

        

    def listInstances(self):
        r = requests.get(self.instanceListURL)
        #print (r.content)

    def changeInstance(self, newInstance):
        r = requests.get(self.instanceListURL)
        if (r.status_code == 200):
            o365InstanceDetails = json.loads(r.content.decode(r.encoding).replace("'",'"'))
            if next((item for item in o365InstanceDetails if item.get("instance") and item["instance"] == newInstance), None) == None:
                instanceNames = []
                for instance in o365InstanceDetails:
                    for k, v in instance.items():
                        if (k == "instance"):
                            instanceNames.append(v)
                raise ValueError("FAILED: Valid instances are " + ', '.join(instanceNames) +".")
            else:
                self.endpointsURL = 'https://endpoints.office.com/endpoints/' + self.o365Instance + '?clientrequestid=' + str(uuid.uuid4())
        else:
            print("Something went wrong")

    def updateJSON(self):
        print(self.endpointsURL)
        print(self.instanceListURL)
        # r = requests.get(endpointsURL)
        # print (r.content)
        # print(r.status_code)
        # print(r.headers['content-type'])
        # print(r.encoding)

# updateJSON()

#print("before __name__ guard")
if __name__ == '__main__':
    #print("Name was __main__")
    o365worldwide = o365Endpoint('Worldwide')
    o365worldwide.updateJSON()
#print("after __name__ guard")


# o365worldwide.updateJSON()
