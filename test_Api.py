import json
import requests
import pytest


class TestAPI(object):
    @pytest.mark.run(order=1)
    def test_get_token(self):
        params = {
            "corpid": "ww63762cffdeedb367",
            "corpsecret": "GmsE-Gy51M3hEI46OSaTR2JpZ7aPpLymBYQjl4SlAxQ"
        }
        res_token = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        return res_token.json()["access_token"]

    def test_get_department_list(self):
        res_get = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.test_get_token()}&id={''}")
        print(res_get.json())
        assert res_get.json()["errcode"] == 0

    def test_add_department(self):
        data = {
            "name": "广州研发中心",
            "parentid": 1,
            "id": 2
        }

        res_add = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.test_get_token()}", data=json.dumps(data))
        print(res_add.json())
        print(res_add.content)
        assert res_add.json()["errcode"] == 0

    def test_update_department(self):
        data = {
            "id": 2,
            "name": "广东研发中心"
        }

        res_update = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.test_get_token()}", json=data)
        print(res_update.json())
        assert res_update.json()["errcode"] == 0

    def test_delete_department(self):

        res_del = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.test_get_token()}&id=2")
        print(res_del.json())
        assert res_del.json()["errcode"] == 0