from SEON.service.Project_Team_Service import Project_Team_Service
from pprint import pprint

team_x = Project_Team_Service()

pprint (team_x.exists('8b65fae0-4577-41cb-89e9-4fae2b1c4ad1'))
pprint (team_x.exists('8b65fae0'))
