import requests

url = "http://www.baidu.com/s"
try:
    kv = {'wd': 'python'}
    r = requests.get(url, params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.request.url)
    print(r.text[:1000])
except:
    print("爬取失败")
