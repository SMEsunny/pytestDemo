import os
from core.rest_client import RestClient
from common.read_data import data


BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]

class User(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)
        
    def register(self, **kwargs):
        return self.post("/register", **kwargs)

    #获取验证码接口
    def get_code(self,phone, **kwargs):
        return self.get("/api/app/appmobile/{}".format(phone), **kwargs)

    #登录，用验证码获取token
    def login(self,**kwargs):
        return self.post("/api/auth/oauth2/token",**kwargs)
    
    def login_out(self, **kwargs):
        return self.delete("/api/auth/token/logout", **kwargs)
    
    def list_all_users(self, **kwargs):
        return self.get("/users", **kwargs)

    def list_one_user(self, username, **kwargs):
        return self.get("/users/{}".format(username), **kwargs)

    def update(self, user_id, **kwargs):
        return self.put("/update/user/{}".format(user_id), **kwargs)

    def delete(self, name, **kwargs):
        return self.post("/delete/user/{}".format(name), **kwargs)


user = User(api_root_url)

