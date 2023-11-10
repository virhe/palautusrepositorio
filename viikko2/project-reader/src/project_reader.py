from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        deserialized = toml.loads(content)
        
        name = deserialized['tool']['poetry']['name']
        description = deserialized['tool']['poetry']['description']
        license = deserialized['tool']['poetry']['license']

        authors = deserialized['tool']['poetry']['authors']

        dependencies = deserialized['tool']['poetry']['dependencies']
        dev_dependencies = deserialized['tool']['poetry']['group']['dev']['dependencies']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)