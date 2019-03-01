from seon.service.Project_Team_Service import Project_Team_Service
from pprint import pprint

team_x = Project_Team_Service()

pprint (team_x.get_by_id_tool('8b65fae0-4577-41cb-89e9-4fae2b1c4ad1'))
