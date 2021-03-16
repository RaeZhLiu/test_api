import json
import requests
import pytest


@pytest.fixture(scope="session")
def get_token():
    params = {
        "corpid": "ww63762cffdeedb367",
        "corpsecret": "GmsE-Gy51M3hEI46OSaTR2JpZ7aPpLymBYQjl4SlAxQ"
    }
    res_token = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
    return res_token.json()["access_token"]


class TestAPI(object):

    def test_get_department_list(self, get_token, id=None):
        res_get = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={get_token}&id={id}")

        return res_get.json()

    def test_add_department(self, get_token, name, parentid, id):
        data = {
            "name": name,
            "parentid": parentid,
            "id": id
        }
        res_add = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={get_token}", data=json.dumps(data))
        return res_add.json()

    def test_update_department(self, get_token, cur_id, name, name_en=None, parentid=None, order=None):
        data = {
            "id": cur_id,
            "name": name,
            "name_en": name_en,
            "parentid": parentid,
            "order": order
        }
        res_update = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={get_token}", json=data)
        return res_update.json()

    def test_delete_department(self, get_token, id):
        res_del = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={get_token}&id={id}")
        return res_del.json()

    info = [("山东研发中心" + str(x), "1", str(x)) for x in range(10, 20)]

    @pytest.mark.parametrize("name, parentid, id", info)
    def test_all(self, get_token, name, parentid, id):
        # 若创建异常
        try:
            assert "created" == self.test_add_department(get_token, name, parentid, id)["errmsg"]
        except AssertionError as e:
            if "department existed" in e.__str__():
                department_info = self.test_get_department_list(get_token)
                num = len(department_info["department"])
                for i in range(num):
                    if department_info["department"][i]["name"] == name:
                        id = department_info["department"][i]["id"]
                        assert "deleted" == self.test_delete_department(get_token, id)['errmsg']
                assert "created" == self.test_add_department(get_token, name, parentid, id)["errmsg"]
        finally:
            assert name in [info["name"] for info in self.test_get_department_list(get_token)["department"]]
            assert "updated" == self.test_update_department(get_token, id, "德州研发中心")["errmsg"]
            assert "deleted" == self.test_delete_department(get_token, id)['errmsg']
