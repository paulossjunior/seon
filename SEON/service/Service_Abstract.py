from requestx.RequestX import RequestX
from pprint import pprint
import json
from collections import namedtuple

class Service_Abstract (object):

    def __init__(self, url = None):
        self.url = url
        self.request_x = RequestX()

    def exists(self, id_tool):

        response = self.get_by_id_tool(id_tool)
        
        if response.status_code == 200:
            return True
        
        return False

    def get_by_id_tool(self, id_tool):
        return self.request_x.get(self.url+'/search/findByIdtool?idtool='+id_tool)

    def connect(self, target_url, from_url):
        return self.request_x.put_uri_list(target_url, from_url)
    
    def update (self, url, data):
        return self.request_x.patch(data, url)

    