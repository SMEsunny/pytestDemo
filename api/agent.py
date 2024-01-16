import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class Agent(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(Agent, self).__init__(api_root_url, **kwargs)

    def list_all_agents(self, **kwargs):
        return self.post("/api/bbs/front/agent/info/square/page/list", **kwargs)
    

agent = Agent(api_root_url)