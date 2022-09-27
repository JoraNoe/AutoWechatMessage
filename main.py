import Gaode
import WeChat

# 获取access_token
def getAccessToken():
    r1 = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            "appid": appID,
            "secret": appsecret
        }
    )
    access_token = r1.json()['access_token']
    # print(access_token)
    return access_token



# 微信id列表 给谁发加谁
wx_id = ["oB63O6s0JNpJPxOtiUDWnGMlMwpI","oB63O6mW5gDQKJyFk2FLXSBdph7E","oB63O6lPUOtE7JaaMfUWUd-9RR7Y"]
# 模板消息id
template_id = 'iPqP0v0KvpQAP_1X_iv79EYpRyD7Q8TyznMV4FGW-no'

# 获取天气数据
weatherData = Gaode.getWeather()

if __name__ == '__main__':
    for a_id in wx_id:
        WeChat.sendMessage(weatherData, a_id, template_id)
