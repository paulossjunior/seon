from .Service_Abstract import Service_Abstract

class Project_Team_Service(Service_Abstract):

    def __init__(self):
        Service_Abstract.__init__(self,'http://localhost:9093/projectteams')
        
    def save (self, name, description, id_tool, url_tool):

        data = {'name': name, 
                'description': description, 
                'idtool': id_tool,
                'urltool': url_tool}
        
        return self.request_x.post(data,self.url)
    
    def get_all (self, organization_url):
        result = self.request_x.get(organization_url+'/projectteams')
        
 
    
    

                
                

                

