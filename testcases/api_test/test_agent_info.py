import pytest
import sys
import allure
from operation.agent import get_all_agent
from testcases.conftest import api_data
from common.logger import logger


# @allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("获取agent信息模块")
class TestGetAgentInfo():
    # """获取agent信息模块"""

    @allure.story("用例--获取全部agent信息")
    @allure.description("该用例是针对获取所有agent信息接口的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.test
    @pytest.mark.parametrize("data,except_result,except_code",
                             api_data["test_get_all_agent_info"])
    def test_get_all_agent_info(self, data,except_result,except_code):
        logger.info("*************** 开始执行用例 ***************")
        size = data["size"]
        current = data["current"]
        query = data["query"]
        result = get_all_agent(size=size,current=current,query=query)
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}, 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        logger.info(result.response.json())
        logger.info("*************** 结束执行用例 ***************")
 


if __name__ == '__main__':
    pytest.main(["-v", "-s", "testcases/api_test/test_agent_info.py"])
