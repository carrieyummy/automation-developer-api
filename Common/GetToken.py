import requests
import json
from Common.RequestsControl import RequestsControl


class GetToken:
    email = "tianyawei@sunseagroup.com"
    pwd = "123456"

    @classmethod
    def user_token(cls, cloud_name):

        if cloud_name == "ct":
            url = "https://aus-ws.ct10649.com:443/users/sign_in"
            app_id = "sunsea-zQ-id"
            app_secret = "sunsea-O7tYPfOPozrsnEN5HOkczUAkGuQ"
        else:
            url = "https://user-dev.sunseaiot.com/users/sign_in"
            app_id = "alya-api-browser-id"
            app_secret = "alya-api-browser-2tFsUL41FELUlyfrSMEZ4kNKwJg"

        header_post = {
            "content-type": "application/json",
            "accept": "application/json"
        }
        data_post = {
            "user": {
                "email": cls.mail,
                "password": cls.pwd,
                "application": {
                    "app_id": app_id,
                    "app_secret": app_secret
                }
            }
        }

        response = RequestsControl.response_text_post(url, header_post, data_post)
        print("获取token……状态码：%s" % response.status_code)
        token_data = response.text
        access_token = json.loads(token_data)["access_token"]
        return access_token

