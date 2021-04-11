from urllib import request

url = 'https://unlock.skihome.xyz' # "MC一言"API
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36'}

def prompt():
    req = request.Request(url=url, headers=headers)
    with request.urlopen(req) as response:
        # 读取response里的内容，并转码
        data = response.read().decode('utf-8') # 默认即为 utf-8
        print(data)
        return data

if __name__ == "__main__":
    pass