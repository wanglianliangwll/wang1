# encodeing:utf-8
import requests
import re
from lxml.html import etree


class Jansuo():
    def __init__(self):
        self.url = "http://law.npc.gov.cn/FLFG/getAllList.action"
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded',
                        'Cookie': 'JSESSIONID=wKgBxhroWm8ivDe1H5fOAUUQrsjCe8lm0-gA',
                        'Host': 'law.npc.gov.cn',
                        'Origin': 'http://law.npc.gov.cn',
                        'Referer': 'http://law.npc.gov.cn/FLFG/getAllList.action?SFYX=%E6%9C%89%E6%95%88&zlsxid=&bmflid=&zdjg=&txtid=&resultSearch=false&lastStrWhere=&keyword=&pagesize=20',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    def start(self):
        data1 = self.data1()
        html = requests.post(url=self.url, data=data1, headers=self.headers).text
        dom_etree = etree.HTML(html)
        all_link = dom_etree.xpath("//a/@href")
        set1 = set()
        for link in all_link:
            if link.startswith("javascript:showLocation"):
                pattery = re.compile('(\d+)')
                num = pattery.search(link).group(0)
                set1.add(num)
        self.again_request(set1)
    def again_request(self,set1):
        for num in set1:
            url = "http://law.npc.gov.cn/FLFG/flfgByID.action?flfgID=" + str(num)
            print(url)

    def data1(self):
        data = {'pagesize': 20,
                'ispage': 1,
                'pageCount': 500,
                'curPage': 1,
                'SFYX': '有效',
                'zlsxid': '03',
                'fenleigengduo': 1,
                'bmflid': '',
                'zdjg': '',
                'txtid': '',
                'resultSearch': 'false',
                'lastStrWhere': '',
                'keyword': ''
                }
        return data
if __name__ == '__main__':
    s = Jansuo()
    s.start()
