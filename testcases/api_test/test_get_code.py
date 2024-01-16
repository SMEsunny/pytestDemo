import pytest
import allure
from operation.user import get_code
from testcases.conftest import api_data
from common.logger import logger


# @allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("获取agent信息模块")
class TestGetCode():
    # """获取agent信息模块"""

    @allure.story("用例--手机号获取验证码")
    @allure.description("该用例是使用手机号获取验证码接口的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.test
    @pytest.mark.parametrize("phone,except_result,except_code,status_code",
                             api_data["test_get_code"])
    def test_get_code(self, phone,except_result,except_code,status_code):
        logger.info("*************** 开始执行用例 ***************")
        result = get_code(phone)
        assert result.response.status_code == status_code
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}, 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        logger.info(result.response.json())
        logger.info("*************** 结束执行用例 ***************")
 


if __name__ == '__main__':
    pytest.main(["-v", "-s", "testcases/api_test/test_get_code.py"])
