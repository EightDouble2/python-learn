import requests

url = "https://m.ip138.com/iplookup.asp?ip="
try:
    r = requests.get(url='202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")
