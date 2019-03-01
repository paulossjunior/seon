from requestx.RequestX import RequestX
from pprint import pprint
from Service import Service

class Project_Team_Service(Service):

    def __init__(self):
        self.url = 'http://localhost:9093/projects'
        

