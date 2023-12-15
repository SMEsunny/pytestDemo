from core.result_base import ResultBase
from api.agent import agent
from common.logger import logger


def get_all_agent(size=10,current=1,query={}):
    """
    获取全部agent信息
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    
    headers = {
        "CLIENT-TOC":"Y",
        "Authorization":"Bearer 77156b36-6fe8-4f97-9a6b-386fb28f31d2"
    }
    json = {
        "size":size,
        "current":current,
        "query":query
    }
    res = agent.list_all_agents(headers=headers,json = json)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()["message"]
    result.response = res
    return result


