import requests
import os

url = "https://i.natgeofe.com/n/0eb2fae7-1cd9-45dd-960f-0c6d39f624df/GettyImages-73504605_4x3.jpg"
root = "images/"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
