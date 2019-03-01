from Service import Service
class Project_Team_Service(Service):

    def __init__(self):
        self.url = 'http://localhost:9093/projectteams'
        

    def save (self, name, description, id_tool, url_tool):

        data = {'name': name, 
                'description': description, 
                'idtool': id_tool,
                'urltool': url_tool}
        
        return self.request_x.post(data,self.url)
    
    
    
    

                
                

                

