import pytest
from base_page.basePage import BasePage
from base_page.public import Public


class Department(BasePage):
    def __init__(self):
        corpsecret = "GmsE-Gy51M3hEI46OSaTR2JpZ7aPpLymBYQjl4SlAxQ"
        self.token = Public().get_token(corpsecret)

    def get_department_list(self, id=None):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
            "params": {
                "access_token": self.token,
                "id": id
            }
        }
        res_get = self.send(data)
        return res_get

    def create_department(self, name, parentid, id=None):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create",
            "params": {
                "access_token": self.token
            },
            "json": {
                "name": name,
                "parentid": parentid,
                "id": id
            }
        }
        res_add = self.send(data)
        return res_add

    def update_department(self, cur_id, name=None, name_en=None, parentid=None, order=None):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/update",
            "params": {
                "access_token": self.token
            },
            "json": {
                "id": cur_id,
                "name": name,
                "name_en": name_en,
                "parentid": parentid,
                "order": order
            }
        }
        res_update = self.send(data)
        return res_update

    def delete_department(self, id):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/delete",
            "params": {
                "access_token": self.token,
                "id": id
            }
        }
        res_del = self.send(data)
        return res_del