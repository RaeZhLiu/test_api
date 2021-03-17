import pytest
from base_page.basePage import BasePage


class Public(BasePage):

    # @pytest.fixture(scope="session")
    def get_token(self, corpsecret):
        params = {
            "corpid": "ww63762cffdeedb367",
            "corpsecret": corpsecret
        }
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "ww63762cffdeedb367",
                "corpsecret": "GmsE-Gy51M3hEI46OSaTR2JpZ7aPpLymBYQjl4SlAxQ"
            }
        }
        res_token = self.send(data)
        return res_token["access_token"]