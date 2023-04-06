from s4api.graphdb_api import GraphDBApi
from s4api.swagger import ApiClient
import json



class GraphDB:

    def __init__(self, endpoint, repo_name):
        self.endpoint = endpoint
        self.repo_name = repo_name
        self.client = ApiClient(endpoint=endpoint)
        self.accessor = GraphDBApi(self.client)
    def query(self, query):
        payload_query = {"query": query}
        response = self.accessor.sparql_select(body=payload_query,
        repo_name=self.repo_name)
        response = json.loads(response)
        return response['results']['bindings']

    def update(self, update):
        payload_update = {"update": update}
        response = self.accessor.sparql_update(body=payload_update,
        repo_name=self.repo_name)
        return response

