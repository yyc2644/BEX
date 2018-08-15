#尝试跑机器人
#目前平台的发布交易，可以通过接口方式实现，用python发送参数来模拟挂单行为
import requests
import json
RequsetUrl  = "http://192.168.1.248:9079/api/transaction/api/v1/user/entrust"
#cookies:
RequestHeaders = {
    "accessToken":"c014811e-f904-41aa-b61d-6e31f0364d05",
    "currLanguage":"zh",
    "Content-Type":"application/json;charset=UTF-8"
}
ByeRequestBody = {"entrustCount":"1","entrustPrice":"1","marketId":31,"":"1","dealPassword":"qwe123"}
ShellRequestBody = {"entrustPrice":"1","entrustCount":"1","marketId":31,"type":"1","dealPassword":"qwe123"}

def entrust(entrustPrice,entrustCount,marketId,Type,dealPassword):
    #委托价格，委托数量，交易对名称，买/卖，确认密码
    {
        "entrustCount":entrustCount,
        "entrustPrice":entrustPrice,
        "marketId":marketId,
        "type":Type,
        "dealPassword":dealPassword
    }



# ByeReq = requests.post(
#     RequsetUrl,
#     data=json.dumps(ByeRequestBody),
#     headers = RequestHeaders
#     )
ShellReq = requests.post(
    RequsetUrl,
    data=json.dumps(entrust(1,1,31,1,"qwe123")),
    headers = RequestHeaders
    )
print(ShellReq.text)



