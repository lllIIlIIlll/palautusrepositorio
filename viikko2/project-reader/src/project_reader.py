from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content_dict = toml.loads(content)
        # print(content_dict)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(content_dict['tool']['poetry']['name'], 
                       content_dict['tool']['poetry']['description'],
                       content_dict['tool']['poetry']['license'],
                       content_dict['tool']['poetry']['authors'],
                       content_dict['tool']['poetry']['dependencies'].keys(), 
                       content_dict['tool']['poetry']['group']['dev']['dependencies'].keys()
                       )
