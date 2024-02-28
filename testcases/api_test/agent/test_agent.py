import pytest
import allure
from operation.agent import *
from testcases.conftest import api_data
from common.logger import logger


# @allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("测试")
@allure.feature("获取agent模块接口")
class Test_agent():

    @allure.story("用例-初始化智能体")
    @allure.description("该用例初始化智能体接口的测试")
    @pytest.mark.parametrize("type,except_result,except_code,status_code",api_data["test_init_agent"])
    def test_init_agent(self,type,except_result,except_code,status_code,get_header_fixture):
        logger.info("*************** 开始执行用例 ***************")
        result = init_agent(headers=get_header_fixture,type=type)
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}, 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        logger.info("*************** 结束执行用例 ***************")
    
 


if __name__ == '__main__':
    pytest.main(["-v", "-s", "testcases/api_test/agent/test_agent.py"])
