import os
import requests
import json
import uuid

class o365Endpoint:
    
    def listInstance(self):
        instanceURL = 'https://endpoints.office.com/version?ClientRequestId=' + str(uuid.uuid4())
        r = requests.get(url)
        print (r.content)

    def __init__(self,o365Instance):
        listInstance(self)
        self.o365Instance = o365Instance

    def updateJSON(self):
        url = 'https://endpoints.office.com/endpoints/' + self.o365Instance + '?clientrequestid=' + str(uuid.uuid4())
        print(url)
        # r = requests.get(url)
        # print (r.content)
        # scriptPath = os.getcwd()
        # outfile = scriptPath + "\\endpoints.json"
        # with open(outfile, 'wb') as f:
        #         f.write(r.content)
        # print(r.status_code)
        # print(r.headers['content-type'])
        # print(r.encoding)

# updateJSON()

o365worldwide = o365Endpoint('Worldwide')

o365worldwide.updateJSON()
