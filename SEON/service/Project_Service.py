from .Service_Abstract import Service_Abstract

class Project_Service(Service_Abstract):

    def __init__(self):
        self.url = 'http://localhost:9093/projects'

    def save (self, name, description, id_tool, url_tool):

        data = {'name': name, 
                'description': description, 
                'idtool': id_tool,
                'urltool': url_tool}
        
        return self.request_x.post(data,self.url)
    def get_all (self, organization_url):
        return self.request_x.get(organization_url+'/projects')