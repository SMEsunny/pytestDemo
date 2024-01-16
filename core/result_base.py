from common.logger import logger


class ResultBase():
    
    #处理通用请求的结果
    def handle_response(self,res):
        logger.info("***********开始处理请求结果****************")
        self.success = False
        logger.info(res.json())
        if res.json()["code"] == 0:
            self.success = True
            self.data = res.json()['data']
        else:
            self.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
        self.msg = res.json()["message"]
        self.response = res
        logger.info("***********处理请求结果完成****************")
        return self
    
        #处理登录请求的结果
    def handle_login_response(self,res):
        self.success = False
        if  res.status_code == 200 and "access_token" in res.json():
            self.success = True
            self.data = res.json()['token_type']+" "+ res.json()['access_token']
        else:
            self.error = "登录接口异常"
        self.response = res
        return self
