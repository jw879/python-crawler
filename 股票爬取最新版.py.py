import requests
from bs4 import BeautifulSoup
import traceback
import re


def get_html_text(url, code='utf-8'):
    '''
    通过指定url链接获取html页面，编码方法默认为utf-8。有简单的错误处理，但不会提示。
    :param url: 指定url
    :param code: 默认为'utf-8'
    :return: 返回相应的html页面信息
    '''
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ''


def get_stock_list(lst, stock_url):
    '''
    获取股票编号并且将它存入列表lst中。
    :param lst: 待存入股票编号的lst
    :param stock_url: 放有股票编号信息的初始url
    :return: 空
    '''
    html = get_html_text(stock_url, 'GB2312')   # 该页面的编码格式为'GB2312'
    soup = BeautifulSoup(html, 'html.parser')
    soupa = soup.find_all('a')
    for a in soupa:
        try:
            href = a.attrs['href']  # 股票编号在html页面中的a标签下的href属性中
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])    # 股票编号的格式为 [s][hz]\d{6}
        except:
            continue


def get_stock_info(lst, stock_url, fpath):
    '''
    通过lst中不同的股票编号爬取在stock_url网站上的不同的股票信息，并存入fpath路径下的.txt文件中
    :param lst: 存放有不同股票的编号的列表
    :param stock_url: 百度股票的始站
    :param fpath: 存放股票信息的.txt文件
    :return:
    '''
    count = 0   # 用来记录当前进度
    # 遍历lst中所有股票编号得到信息
    for stock in lst:
        # 构造url获取html页面
        url = stock_url + stock + ".html"
        html = get_html_text(url)
        try:
            # 将html页面做成beautiful汤
            if html == "":
                continue
            info_dict = {}
            soup = BeautifulSoup(html, 'html.parser')

            # 使用beautiful soup功能函数获取到相关信息(股票名称，最高，最低，今开，作收........)
            stock_info = soup.find('div', attrs={'class': 'stock-bets'})
            name = stock_info.find_all(attrs={'class': 'bets-name'})[0]
            key_list = stock_info.find_all('dt')
            value_list = stock_info.find_all('dd')
            if len(key_list) == 0:  # 说明该股票没有信息
                continue

            # 将信息存入info_dict
            info_dict.update({'股票名称': name.text.split()[0]})
            for i in range(len(key_list)):
                key = key_list[i].text
                value = value_list[i].text
                info_dict[key] = value

            # 将信息写入文件，并打印当前进度
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(info_dict)+'\n')
                count = count + 1
                print('\r当前进度：{:.2f}%'.format(count*100/len(lst)), '[', '*'*int(count*50/len(lst)),
                      '-'*int(50 - count*50/len(lst)), ']', end='')

        except:
            # 一两只股票的失败不影响大局。
            count = count + 1
            print('\r当前进度：{:.2f}%'.format(count * 100 / len(lst)), '[', '*' * int(count * 50 / len(lst)),
                  '-' * int(50 - count * 50 / len(lst)), ']', end='')
            # traceback.print_exc()  本函数可以配合try except来补捉bug
            continue


if __name__ == "__main__":
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'G://BaiDuStockInfo.txt'
    slist = []
    get_stock_list(slist, stock_list_url)
    get_stock_info(slist, stock_info_url, output_file)