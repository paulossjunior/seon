from SEON.service.Project_Team_Service import Project_Team_Service
from SEON.service.Project_Service import Project_Service
from pprint import pprint

team_x = Project_Team_Service()
projct_x = Project_Service()

pprint (team_x.exists('8b65fae0-4577-41cb-89e9-4fae2b1c4ad1'))
pprint (team_x.exists('8b65fae0'))

projct_x.connect('https://enterprise-ontology-service.herokuapp.com/organizations/1',
                'https://enterprise-ontology-service.herokuapp.com/projects/1')
