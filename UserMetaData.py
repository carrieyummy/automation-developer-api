from Common.GetToken import *
from Common.RequestsControl import *


class UserMetaData:

    response = RequestsControl()

    # UserMetaData接口的地址，此处是天翼云后台时的地址
    url = "https://aus-ws.ct10649.com:443/api/v1/users/data"
    # 测试隐藏OEM用户时，被测用户的uuid
    uuid = "204f3342-6d23-11e8-a51d-0a580af40501"
    # value值为forbidden时，用户被隐藏
    value = "forbidden"
    # 获取token
    token = GetToken.user_token("ct")

    print("本次请求使用的token：%s" % token)
    print("被测用户uuid：%s" % uuid)
    request_headers = {
        "Authorization": "auth_token %s" % token,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    request_data = {
        "key": uuid,
        "value": value
    }

    # 1 根据key值，返回符合筛选条件的结果。可返回多条。——测试隐藏OEM用户时不太需要用到。
    def get_user_data(self):
        self.response = RequestsControl.response_text_get(self.url, self.uuid, self.request_headers)
        return self.response

    # 2 隐藏指定的用户，设置value值为forbidden
    def post_create_new_datum(self):
        self.response = RequestsControl.response_text_post(self.url, self.request_headers, self.request_data)
        return self.response

    # 3 查询，返回单条结果
    def get_specific_user_datum(self):
        self.response = RequestsControl.response_text_get(self.url, self.uuid, self.request_headers, 2)
        return self.response

    # 4 修改value值
    def update_specific_datum(self, value):
        del self.request_data["key"]
        self.request_data["value"] = value
        self.response = RequestsControl.response_text_put(self.url, self.uuid, self.request_headers, self.request_data)
        return self.response

    # 5 删除。——测试隐藏OEM用户时，删除后用户恢复显示。
    def delete_specific_datum(self):
        self.response = RequestsControl.response_text_delete(self.url, self.uuid, self.request_headers)
        return self.response


if __name__ == '__main__':
    usermetadata = UserMetaData()
    # 修改uer_config和edit_value的值，控制所做的操作。
    user_config = 1
    edit_value = "forbid"

    if user_config == 1:
        response = usermetadata.get_user_data()
    elif user_config == 2:
        response = usermetadata.post_create_new_datum()
    elif user_config == 3:
        response = usermetadata.get_specific_user_datum()
    elif user_config == 4:
        response = usermetadata.update_specific_datum(edit_value)
    elif user_config == 5:
        response = usermetadata.delete_specific_datum()

    print("本次返回的状态码：%s" % response.status_code)
    if user_config == 5:
        print("本次返回的参数：%s" % response.headers)
    else:
        print("本次返回的参数：%s" % response.json())
