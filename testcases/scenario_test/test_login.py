import pytest
import allure
from operation.user import get_code,login
from common.logger import logger


@allure.step("步骤1 ==>> 获取验证码")
def step_1(phone):
    logger.info("步骤1 ==>> 获取验证码 ==>> {}".format(phone))


@allure.step("步骤2 ==>> 使用验证码登录")
def step_2(phone,code):
    logger.info("步骤2 ==>> 登录用户：{},{}".format(phone,code))


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户获取验证码并使用验证码登录")
class TestRegLogList():

    @allure.story("用例--获取验证码/登录--预期成功")
    @allure.description("该用例是针对 使用验证码登录 场景的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("用户获取验证码/登录-预期成功")
    @pytest.mark.multiple
    def test_user_login(self):

        logger.info("*************** 开始执行用例 ***************")
        phone = "18011111118"
        result = get_code(phone)
        code = result.data
        step_1(phone)
        assert result.success is True, result.error
        result = login(phone,code)
        step_2(phone,code)
        assert result.success is True, result.error
        logger.info("*************** 登录成功,token为{}***************".format(result.data))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "testcases/scenario_test/test_login.py"])
