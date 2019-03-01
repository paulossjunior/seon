from requestx.RequestX import RequestX

class Project_Team_Service(object):

    def __init__(self):
        self.url = 'http://localhost:9093/projectteams'
        self.request_x = RequestX()

    def save (self, name, description, id_tool, url_tool):

        data = {'name': name, 
                'description': description, 
                'idtool': id_tool,
                'urltool': url_tool}
        
        return self.request_x.post(data,self.url)
    
    def get_by_id_tool(self, id_tool):

        return self.request_x.get(self.url+'/search/findByIdtool?idtool='+id_tool)

    def connect_organization_project_team(self, organization_url, project_team_url):
        return self.request_x.put_uri_list(organization_url, project_team_url)

                
                

                

