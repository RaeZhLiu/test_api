import pytest
import requests


class BasePage(object):
    def send(self, data):
        return requests.request(**data).json()