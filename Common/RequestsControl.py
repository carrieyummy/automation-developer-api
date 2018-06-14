import requests
import json


class RequestsControl:

    @classmethod
    def response_text_post(cls, url, header_post, data_post):
        print("Post请求，接口地址：%s" % url)
        s = requests.session()
        r_post = s.post(url=url, headers=header_post, data=json.dumps(data_post))
        s.close()
        return r_post

    # 默认option是1，通过option的值决定接口地址
    @classmethod
    def response_text_get(cls, url, uuid, header_get, option=1):
        if option == 1:
            get_url = "%s?keys=%s" % (url, uuid)
        else:
            get_url = "%s/%s" % (url, uuid)

        print("Get请求，接口地址：%s" % get_url)
        s = requests.session()
        r_get = s.get(url=get_url, headers=header_get)
        s.close()
        return r_get

    @classmethod
    def response_text_delete(cls, url, uuid, header_delete):
        delete_url = "%s/%s" % (url, uuid)
        print("Delete请求，接口地址：%s" % delete_url)
        s = requests.session()
        r_delete = s.delete(url=delete_url, headers=header_delete)
        s.close()
        return r_delete

    @classmethod
    def response_text_put(cls, url, uuid, header_put, data_put):
        put_url = "%s/%s" % (url, uuid)
        print("Put请求，接口地址：%s" % url)
        s = requests.session()
        r_put = s.put(url=put_url, headers=header_put, data=json.dumps(data_put))
        s.close()
        return r_put
