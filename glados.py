# import requests
# import json
# import os

# url = "https://glados.rocks/api/user/checkin"
# data = {"token":"glados.one"}
# cookie = os.environ.get("GLADOS_COOKIE", "")
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.141 Safari/537.36",
#     "Cookie": cookie
# }

# print(cookie)
# response = requests.post(url, data=data, headers=headers)
# try:
#     print(json.loads(response.text)['message'])
# except:
#     print(response.text)
#     print("cookie失效")

import os
print(os.environ.get("GLADOS_COOKIE", "oh no"))