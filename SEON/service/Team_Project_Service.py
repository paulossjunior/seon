import requests
import json
class Team_Project_Service(object):

    def __init__(self):
        self.headers_post = {'Content-type': 'application/json', 'Accept': 'application/json'}
        self.headers_uri_list = {'Content-type': 'text/uri-list', 'Accept': 'application/json'}
        self.url = 'http://localhost:9093/projectteams'

    def save (self, name, description, id_tool, url_tool):

        data = {'name': name, 
                'description': description, 
                'idtool': id_tool,
                'urltool': url_tool}
        
        return self.__post(data)
    
    def connect_organization_team_project(self, organization_url, team_project_url):
        return self.__put_uri_list(organization_url, team_project_url)

    def __post(self,data):
        response = requests.post(self.url, 
                                json=data,headers=self.headers_post)
        return response.json()
    
    def __put_uri_list (self,data, url):
        response = requests.put(url, data=data,headers=self.headers_uri_list)
        return response.json()
                
                

                

