# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import re


def login(username, password):
    url1 = "https://api-user.huami.com/registrations/+86" + username + "/tokens"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2"
    }
    data = {
        "client_id": "HuaMi",
        "password": f"{password}",
        "redirect_uri": "https://s3-us-west-2.amazonaws.com/hm-registration/successsignin.html",
        "token": "access"
    }
    r1 = requests.post(url1, data, headers, allow_redirects=False)
    location = r1.headers["Location"]
    try:
        code_pattern = re.compile("(?<=access=).*?(?=&)")
        code = code_pattern.findall(location)[0]
        print("access_code获取成功！")
    except:
        return 0, 0

    url2 = "https://account.huami.com/v2/client/login"
    data2 = {
        "app_name": "com.xiaomi.hm.health",
        "app_version": "4.6.0",
        "code": f"{code}",
        "country_code": "CN",
        "device_id": "2C8B4939-0CCD-4E94-8CBA-CB8EA6E613A1",
        "device_model": "phone",
        "grant_type": "access_token",
        "third_name": "huami_phone",
    }
    r2 = requests.post(url2, data=data2, headers=headers).json()
    login_token = r2["token_info"]["login_token"]
    print("login_token获取成功！===", login_token)
    userid = r2["token_info"]["user_id"]
    return login_token, userid


def changeStep(username, password, step):
    print('开始')
    login_token, userid = login(username, password)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')
    changeStep('', '', 12000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
