# 爬取天气网上的数据
import requests

HEADS = {
    "Referer": "http://www.weather.com.cn/weather1d/101210101.shtml",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/85.0.4183.83 Safari/537.36",
    "Host": "toy1.weather.com.cn"
}


def get_city_w_id(name):
    url_str = "http://toy1.weather.com.cn/search?cityname=" + name
    r = requests.get(url_str, headers=HEADS)
    value = None
    if r.status_code == 200:
        value = r.text
        print(value)
    return value
