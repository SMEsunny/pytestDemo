from common.util import get_dynamic_headers
from core.result_base import ResultBase
from api.agent import agent
from common.logger import logger


def get_all_agent(size=16,current=1,query={},token=""):
    """
    获取全部agent信息
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    dynamic_headers =get_dynamic_headers()
    headers = {
        "CLIENT-TOC":"Y",
        "Authorization":token,
        "abc12":dynamic_headers["abc12"],
        "aee":dynamic_headers["aee"],
        "timeStamp":dynamic_headers["timeStamp"]
    }
    json = {
        "size":size,
        "current":current,
        "query":query
    }
    res = agent.list_all_agents(headers=headers,json = json)
    return result.handle_response(res)



