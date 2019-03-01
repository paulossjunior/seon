from requestx.RequestX import RequestX
from pprint import pprint
from .Service_Abstract import Service_Abstract

class Project_Team_Service(Service_Abstract):

    def __init__(self):
        Service_Abstract.__init__(self,'http://localhost:9093/projects')
        

