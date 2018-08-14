#尝试跑机器人
#目前平台的发布交易，可以通过接口方式实现，用python发送参数来模拟挂单行为
import urllib
import requests
import json
RequsetUrl  = "http://192.168.1.248:9079/api/transaction/api/v1/user/entrust"
#cookies:
RequestHeaders = {
    "accessToken":"c014811e-f904-41aa-b61d-6e31f0364d05",
    "currLanguage":"zh",
    "Content-Type":"application/json;charset=UTF-8"
}
RequestBody = {"entrustPrice":"1","entrustCount":"1","marketId":31,"type":"1","dealPassword":"qwe123"}

request = requests.session()

req = requests.post(RequsetUrl,data=json.dumps(RequestBody),headers = RequestHeaders)
# header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
print(req.text)

# REQ = requests('psot',RequsetUrl，data = RequestBody,)

#     return request('post', url, data=data, json=json, **kwargs)

 