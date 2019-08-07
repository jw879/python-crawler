import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/75.0.3770.100 Safari/537.36"}


# 1.提交商品搜索请求，循环获取页面
def get_html_text(url):
    try:
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("异常")
        return ""


# 2.对于每个页面，提取商品名称和价格信息
def parse_page(page, ilt, html):
    # print(html.text[:1000])
    try:
        plt = re.findall(r'165;[\d.|,]*', html)   # 价格
        tlt = re.findall(r'shopID=\d{1,4}">[(\u4e00-\u9fa5)|\w|（|）| |/]+</a>', html)
        for i in range(len(plt)):
            price = plt[i].split(';')[1]
            title = tlt[i].split('>')[1][:-3]
            ilt.append([price, title])
    except:
        print("parse_page({})异常".format(page))


# 3.将信息打印
def print_goods_list(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


if __name__ == '__main__':
    goods = '手机'
    depth = 7
    # start_url = 'https://s.taobao.com/search?q=' + goods
    start_url = 'http://www.furuima.cn/Search/Index?p={}&id=' + goods
    infolist = []
    for i in range(depth):
        if i != 0:
            try:
                url = start_url.format(i)
                print(url)
                html = get_html_text(url)
                parse_page(i, infolist, html)
            except:
                continue
    print_goods_list(infolist)