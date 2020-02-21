import requests
from lxml import etree
import os
from selenium import webdriver
import header_a
import header_c
import random
import re
import csv
import pandas as pd
import pandas
import sqlite3
import wordninja
from bottle import route, run, template, request, static_file, redirect


class Spider_Amazon(object):

    def __init__(self):
        self.start_url = 's?k=' + p
        self.base_url = 'www.amazon.com/'
        self.headers = header_a.HEADERS
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\Desktop\chromedriver\chromedriver.exe")
        self.urlset = set()
        self.titleset = set()

    def get(self, url):
        header = random.choice(self.headers)
        response = requests.get(url=url, headers=header, timeout=10)
        return response.content

    def parse_url(self, url):
        print(url)
        header = random.choice(self.headers)
        response = requests.get(url=url, headers=header, timeout=10)
        assert response.status_code == 200
        xhtml = etree.HTML(response.content)
        return xhtml

    def get_base_url_list(self):
        if os.path.exists(header_a.BASE_URL_LIST_FILE):
            li = self.read_base_url_list()
            return li
        url_list = []
        self.save_base_url_list(url_list)

        return url_list

    def save_base_url_list(self, base_url_list):
        with open(r"C:\Users\Administrator\Desktop\python\pycharm1\url_a.txt", "w") as f:
            for u in base_url_list:
                f.write(self.base_url + u + "\n")

    def read_base_url_list(self):
        with open(r"C:\Users\Administrator\Desktop\python\pycharm1\url_a.txt", "r") as f:
            line = f.readlines()
        li = [s.strip() for s in line]
        return li

    def driver_get(self, url):
        try:
            self.driver.set_script_timeout(5)
            self.driver.get(url)
        except:
            self.driver_get(url)

    def run(self):
        base_url_list = self.get_base_url_list()
        data_list = []
        data_list_amazon_price = []
        data_list_amazon_item = []
        for url in base_url_list:
            self.driver_get(url)
            html = self.driver.page_source
            xhtml = etree.HTML(html)
            a_list = xhtml.xpath('//div[@class="sg-col-inner"]/div/h2/a')
            for a in a_list:
                title = a.xpath(".//span/text()")
                url = a.xpath(".//@href")
                url = self.base_url + url[0]
                data_list.append([title, url])
                data_list_amazon_price.append([url])
                data_list_amazon_item.append([title])
                self.urlset.add(url)
                data1 = pd.DataFrame(data_list, columns=["Title", "url"])
                #data2 = pd.DataFrame(data_list_amazon_price, columns=["url"])
                data3 = pd.DataFrame(data_list_amazon_item, index=None)
                data1.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\tu_a.csv")
                # data1.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\tu_a1.csv", header=None, index=None)
                #data2.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a1.txt")
                data3.to_csv(r"C:\Users\Administrator\Desktop\index_a.csv", header=None, index=None)

    def run2(self):
        base_url_list = self.get_base_url_list()
        data_list_amazon_price = []
        for url in base_url_list:
            self.driver_get(url)
            html = self.driver.page_source
            xhtml = etree.HTML(html)
            # //div[@class='sg-col-inner']/div[@class='a-section a-spacing-none a-spacing-top-small']/div[2]/div/a[1]/span[@class='a-price']/span[1]/text()
            a_list = xhtml.xpath('//div[@class="sg-col-inner"]')
            for a in a_list:
                title = a.xpath(".//div/h2/a/span/text()")
                price = a.xpath(
                    ".//div[@class='a-section a-spacing-none a-spacing-top-small']/div[2]/div/a[1]/span[@class='a-price']/span[1]/text()")
                data_list_amazon_price.append([title, price])
                data2 = pd.DataFrame(data_list_amazon_price, columns=["Title", "Price"])
                data2.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a5.csv", index=None)


class Spider_Chegg(object):

    def __init__(self):
        self.start_url = 'search/' + p
        self.base_url = 'www.chegg.com/'
        self.headers = header_c.HEADERS
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\Desktop\chromedriver\chromedriver.exe")
        self.urlset = set()
        self.titleset = set()

    def get(self, url):
        header = random.choice(self.headers)
        response = requests.get(url=url, headers=header, timeout=10)
        return response.content

    def parse_url(self, url):
        print(url)
        header = random.choice(self.headers)
        response = requests.get(url=url, headers=header, timeout=10)
        assert response.status_code == 200
        xhtml = etree.HTML(response.content)
        return xhtml

    def get_base_url_list(self):
        if os.path.exists(header_c.BASE_URL_LIST_FILE):
            li = self.read_base_url_list()
            return li
        url_list = []
        self.save_base_url_list(url_list)

        return url_list

    def save_base_url_list(self, base_url_list):
        with open(r"C:\Users\Administrator\Desktop\python\pycharm1\url_c.txt", "w") as f:
            for u in base_url_list:
                f.write(self.base_url + u + "\n")

    def read_base_url_list(self):
        with open(r"C:\Users\Administrator\Desktop\python\pycharm1\url_c.txt", "r") as f:
            line = f.readlines()
        li = [s.strip() for s in line]
        return li

    def driver_get(self, url):
        try:
            self.driver.set_script_timeout(5)
            self.driver.get(url)
        except:
            self.driver_get(url)

    def run(self):
        base_url_list = self.get_base_url_list()
        data_list = []
        data_list_title_c = []
        for url in base_url_list:
            self.driver_get(url)
            html = self.driver.page_source
            xhtml = etree.HTML(html)
            a_list = xhtml.xpath('//div[@class="sc-jrIrqw fgbpRK"]/a')
            for a in a_list:
                url = a.xpath(".//@href")
                title1 = a.xpath(".//div[2]/div/div/div/em/text()")
                title2 = a.xpath(".//div[2]/div/div/div/text()")
                title = title2 + title1
                url = self.base_url + url[0]
                data_list.append([title, url])
                data_list_title_c.append([title])
                self.urlset.add(url)
                data = pd.DataFrame(data_list, columns=["Title", "url"])
                data.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\tu_c.csv")
                data.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\tu_c1.csv")
                data2 = pd.DataFrame(data_list_title_c)
                data2.to_csv(r"C:\Users\Administrator\Desktop\index_c.csv", header=None, index=None)


q = r'\s*\d+(.*)'


def clean_amazon_price(text):
    c = re.compile(q)
    lists = []
    lines = text.split('\n')
    for line in lines:
        r = c.findall(line)
        if r:
            lists.append(r[0])

    return '\n'.join(lists)


class Spider_Amazon_Price(object):

    def __init__(self):
        self.base_url = 'www.amazon.com/'
        self.headers = header_a.HEADERS
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\Desktop\chromedriver\chromedriver.exe")
        self.urlset = set()
        self.titleset = set()

    def get(self, url):
        header = random.choice(self.headers)
        response = requests.get(url=url, headers=header, timeout=10)
        return response.content

    def parse_url(self, url):
        print(url)
        header = random.choice(self.headers)
        response = requests.get(url=url, headers=header, timeout=10)
        assert response.status_code == 200
        xhtml = etree.HTML(response.content)
        return xhtml

    def get_base_url_list(self):
        if os.path.exists(header_a.BASE_URL_LIST_FILE1):
            li = self.read_base_url_list()
            return li
        url_list = []
        self.save_base_url_list(url_list)

        return url_list

    def save_base_url_list(self, base_url_list):
        with open(R"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a3.txt", "w") as f:
            for u in base_url_list:
                f.write(self.base_url + u + "\n")

    def read_base_url_list(self):
        with open(R"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a3.txt", "r") as f:
            line = f.readlines()
        li = [s.strip() for s in line]
        return li

    def driver_get(self, url):
        try:
            self.driver.set_script_timeout(5)
            self.driver.get(url)
        except:
            self.driver_get(url)

    def run(self):
        base_url_list = self.get_base_url_list()
        # data_list = []
        data_list_amazon_price = []
        for url in base_url_list:
            self.driver_get(url)
            html = self.driver.page_source
            xhtml = etree.HTML(html)
            a_list = xhtml.xpath('//div[@class="a-row"]/div[2]')
            # //div[@class = 'a-row']/div[2]/span[@id = 'rentPrice']/text()
            for a in a_list:
                title = a.xpath(".//span[@id = 'rentPrice']/text()")
                # //span[@class = 'a-list-item']/span/span/a/span[@class = 'a-color-base']/span/text()   price xpath amazon
                # //div[@class='sg-col-inner']/div[@class='a-section a-spacing-none a-spacing-top-small']/div[2]/div/a[1]/span[@class='a-price']/span[1]/text()
                # url = a.xpath(".//@href")
                # url = self.base_url + url[0]
                # data_list.append([title, url])
                data_list_amazon_price.append([title])
                # self.urlset.add(url)
                data1 = pd.DataFrame(data_list_amazon_price, columns=["Price"])
                # data2 = pd.DataFrame(data_list_amazon_price, columns=["url"])
                data1.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\p_a.csv")
                # data2.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a1.txt")


@route('/')
def index():
    return redirect("/hello/")


@route('/hello/')
def index():
    form = request.GET.decode('gbk')
    keyword = form.get("keyword", "")
    cut = list(wordninja.split(keyword))
    page_id_list = get_page_id_list_from_key_word_cut(cut)
    page_list = get_page_list_from_page_id_list(page_id_list)
    page_list1 = get_page_list_from_page_id_list1(page_id_list)
    page_list = sort_page_list(page_list, cut)
    page_list1 = sort_page_list1(page_list1, cut)
    context = {
        "page_list": page_list[:20],
        "keyword": keyword,
        "page_list1": page_list1[:20],
        "keyword": keyword
    }
    return template(r"C:\Users\Administrator\Desktop\python\pycharm1\searcher.html", context)

def sort_page_list(page_list, cut):
    con_list = []
    for page in page_list:
        url = page[2]
        words = page[1]
        title = page[3]
        vector = words.split(" ")
        same = 0
        for i in vector:
            if i in cut:
                same += 1
        cos = same / (len(vector)*len(cut))
        con_list.append([cos, url, words, title])
    con_list = sorted(con_list, key=lambda i: i[0], reverse=True)
    return con_list

def get_page_list_from_page_id_list(page_id_list):
    id_list = "("
    for k in page_id_list:
        id_list += "%s,"%k
    id_list = id_list.strip(",") + ")"
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\amazon_info.db")
    c = conn.cursor()
    sql = "select * " \
          + "from page_info1  " \
          + "where id in " + id_list + ";"
    res = c.execute(sql)
    res = [r for r in res]
    return res
def get_page_id_list_from_key_word_cut(cut):
    keyword = "("
    for k in cut:
        if k == " ":
            continue
        keyword += "'%s',"%k
    keyword = keyword.strip(",") + ")"
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\amazon_info.db")
    c = conn.cursor()
    sql = "select page_id " \
          + "from page_index1  " \
          + "where keyword in " + keyword + ";"
    res = c.execute(sql)
    res = [r[0] for r in res]
    return res

def sort_page_list1(page_list1, cut):
    con_list = []
    for page in page_list1:
        url = page[2]
        words = page[1]
        title = page[3]
        vector = words.split(" ")
        same = 0
        for i in vector:
            if i in cut:
                same += 1
        cos = same / (len(vector)*len(cut))
        con_list.append([cos, url, words, title])
    con_list = sorted(con_list, key=lambda i: i[0], reverse=True)
    return con_list


def get_page_list_from_page_id_list1(page_id_list):
    id_list = "("
    for k in page_id_list:
        id_list += "%s,"%k
    id_list = id_list.strip(",") + ")"
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\chegg_info.db")
    c = conn.cursor()
    sql = "select * " \
          + "from page_info2  " \
          + "where id in " + id_list + ";"
    res = c.execute(sql)
    res = [r for r in res]
    return res
def get_page_id_list_from_key_word_cut1(cut):
    keyword = "("
    for k in cut:
        if k == " ":
            continue
        keyword += "'%s',"%k
    keyword = keyword.strip(",") + ")"
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\chegg_info.db")
    c = conn.cursor()
    sql = "select page_id " \
          + "from page_index2  " \
          + "where keyword in " + keyword + ";"
    res = c.execute(sql)
    res = [r[0] for r in res]
    return res


if __name__ == '__main__':
    p = input("please enter a book name: ")
    print("Start Amazon data collection")
    print("------------------------------------------------")
    f = open(r"C:\Users\Administrator\Desktop\python\pycharm1\url_a.txt", "w")
    f.write('http://www.amazon.com/' + 's?k=' + p + '\n')
    # f.write('https://www.amazon.com/s?k=' + p + '&page=2' + '\n')
    f.close()
    s = Spider_Amazon()
    s.run()
    s.run2()
    print("Have finished Amazon data collection")
    print("------------------------------------------------")
    print("Start Chegg data collection")
    f = open(r"C:\Users\Administrator\Desktop\python\pycharm1\url_c.txt", "w")
    f.write('http://www.chegg.com/' + 'search/' + p + '\n')
    # f.write('https://www.chegg.com/search/' + p + '#p=2' + '\n')
    f.close()
    k = Spider_Chegg()
    k.run()
    print("------------------------------------------------")
    print("Have finished Amazon data collection")
    print("------------------------------------------------")
    print("Start building Amazon page info")
    print("------------------------------------------------")
    # 从tu_a到u_a590
    # 最后产生的u_a56为Amazon的page_info
    # 590是pageinfo
    # 616是pageindex
    # 最后的56需要整理一下keyword
    dt = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\tu_a.csv")
    dt.columns = ["price", "Title", "url"]
    dt = dt.drop(['price'], axis=1)
    dt.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\tu_a1.csv", index=None, header=None)
    dt = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a9.csv")
    dr = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\tu_a1.csv")
    de = pd.concat([dt, dr], axis=1)
    de = pd.DataFrame(de)
    de.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a10.csv", index=None)
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a10.csv")
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a110.csv")
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a10.csv")
    df.columns = ["Title", "price", "title", "url"]
    df = df.dropna(axis=0, how='any')
    df['Title'] = df['title']
    df['title'] = df['title'].map(str.lower)
    df['Title'] = df['title'] + df['Title']
    df['title'] = df['title'].map(str.upper)
    df['Title'] = df['title'] + df['Title']
    df = df.drop(['title'], axis=1)
    df = df.drop(['price'], axis=1)
    # df = df.dropna(axis=0, how='any')
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a11.csv")
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a11.csv")
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a50.csv", index=None)

    # 进行分类整理，使用的是totol整理模式

    ft0 = r'\[|\]|\,|\''
    ft1 = r'\s\s'
    dw = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a50.csv")
    dw.columns = ["id", "title", "url"]
    dw.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a51.csv")
    de = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a51.csv")
    de = de.dropna(axis=0, how='any')
    de.columns = ["Num", "id", "title", "url"]
    de['ik1'] = de.apply(lambda x: re.sub(ft0, '', x['title']).strip(), axis=1)
    de['keyword'] = de.apply(lambda x: re.sub(ft1, '', x['ik1']).strip(), axis=1)
    de.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a52.csv", index=None)
    dr = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a52.csv")
    dr['id'] = dr['keyword']
    dr['ik1'] = dr['title']
    dr['title'] = dr['url']
    dr = dr.drop(['keyword'], axis=1)
    dr = dr.drop(['url'], axis=1)
    dr.columns = ["id", "keyword", "url", "title"]
    dr['title'] = dr['keyword']
    dr.loc[dr.id >= 0, 'url'] = "https://" + dr.url
    dr.loc[dr.id >= 0, 'id'] = 1000 + dr.id
    dr.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a53.csv", index=None)

    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a53.csv")
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a54.csv")
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a54.csv")
    df.columns = ["num", "id", "keyword", "url", "title"]
    df.loc[df.id >= 0, 'num'] = 1000 + df.num
    df = df.drop(["id"], axis=1)
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a55.csv", index=None)
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a55.csv")
    df.columns = ["id", "keyword", "url", "title"]
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a56.csv", index=None)

    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a110.csv")
    df.columns = ["1", "2", "3", "4", "5"]
    df = df.dropna(axis=0, how='any')
    df = df.drop(["1"], axis=1)
    df = df.drop(["2"], axis=1)
    df = df.drop(["3"], axis=1)
    df = df.drop(["5"], axis=1)
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a111.csv", index=None)
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a111.csv")
    df.columns = ["name"]
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a112.csv", index=None)
    ft3 = r'\[|\]|\,|\''
    dt = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a56.csv")
    dr = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a112.csv")
    de = pd.concat([dt, dr], axis=1)
    de = pd.DataFrame(de)
    de.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a570.csv", index=None)
    dt = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a570.csv")
    dt['keyword'] = dt['name']
    dt = dt.drop(['name'], axis=1)
    dt.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a580.csv", index=None)
    dt = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a580.csv")
    dt['title'] = dt['keyword']
    dt['title'] = dt.apply(lambda x: re.sub(ft3, '', x['title']).strip(), axis=1)
    dt.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a590.csv", index=None)
    print("Finished")
    print("------------------------------------------------")
    print("Start building Amazon page index")
    print("------------------------------------------------")
    # 这一段是制作page_index
    ft4 = r'\[|\]|\,|\''
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a590.csv")
    df["title"] = df['title'].map(str.lower)
    df["keyword"] = df["keyword"] + df["title"]
    df["title"] = df['title'].map(str.upper)
    df["keyword"] = df["keyword"] + df["title"]
    df['keyword'] = df.apply(lambda x: re.sub(ft4, '', x['keyword']).strip(), axis=1)
    df = df.drop(["id"], axis=1)
    df = df.drop(["title"], axis=1)
    df = df.drop(["url"], axis=1)
    # ua_610与桌面上的999为同一个文件
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a610.csv", header=None)
    # 999到1117
    ft5 = r'\d\d\d'
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    with open(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a610.csv", encoding='utf8') as f:
        data = f.readlines()
        r = 1000
        for i in data:
            k = wordninja.split(i)
            i.replace('[', ' ')
            i.replace(']', ' ')
            i.replace("’", " ")
            i.replace("'", " ")
            for y in k:
                r = str(r)
                list2 = [r + l for l in k]
            list3.extend(list2)
            r = int(r)
            r = r + 1
        for q in list3:
            list4.append(q)
            s = q[0:]
            o = pd.DataFrame(list4)
            o.index.name = None
            o.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a611.csv", header=None,
                     index=None)
    ft6 = r'\d\d\d\d'
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a611.csv")
    df['id'] = df.apply(lambda x: re.match(ft6, x["10000"]).group(), axis=1)
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a612.csv", index=None)
    dk = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a612.csv")
    dk['10000'] = dk.replace(re.compile(ft6), '')
    dk['10000'] = dk.replace("'", "Nan")
    dk = dk[~dk['10000'].isin(['Nan'])]
    dk.reset_index()
    dk.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a613.csv", header=None)
    dr = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a613.csv")
    dr.columns = ["id", "keyword", "page_id"]
    dr.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a614.csv", index=None)
    dr = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a614.csv")
    dr = dr.drop(['id'], axis=1)
    dr.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a615.csv")
    dr = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a615.csv")
    dr.columns = ["id", "keyword", "page_id"]
    dr.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a616.csv", index=None)
    print("Finished")
    print("------------------------------------------------")
    print("Start building Chegg page info")
    print("------------------------------------------------")

    #chegg
    dt = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\tu_c.csv")
    dt.columns = ["price", "Title", "url"]
    dt = dt.drop(['price'], axis=1)
    dt.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\tu_c1.csv", index=None, header=None)
    dt = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\tu_c1.csv")

    dr = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\tu_c1.csv")
    de = pd.concat([dt, dr], axis=1)
    de = pd.DataFrame(de)
    de.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c10.csv", index=None)
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c10.csv")
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c110.csv")
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c10.csv")
    df.columns = ["Title", "price", "title", "url"]
    df = df.dropna(axis=0, how='any')
    df['Title'] = df['title']
    df['title'] = df['title'].map(str.lower)
    df['Title'] = df['title'] + df['Title']
    df['title'] = df['title'].map(str.upper)
    df['Title'] = df['title'] + df['Title']
    df = df.drop(['title'], axis=1)
    df = df.drop(['price'], axis=1)
    # df = df.dropna(axis=0, how='any')
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c11.csv")
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c11.csv")
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c50.csv", index=None)

    # 进行分类整理，使用的是totol整理模式

    ft0 = r'\[|\]|\,|\''
    ft1 = r'\s\s'
    dw = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c50.csv")
    dw.columns = ["id", "title", "url"]
    dw.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c51.csv")
    de = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c51.csv")
    de = de.dropna(axis=0, how='any')
    de.columns = ["Num", "id", "title", "url"]
    de['ik1'] = de.apply(lambda x: re.sub(ft0, '', x['title']).strip(), axis=1)
    de['keyword'] = de.apply(lambda x: re.sub(ft1, '', x['ik1']).strip(), axis=1)
    de.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c52.csv", index=None)
    dr = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c52.csv")
    dr['id'] = dr['keyword']
    dr['ik1'] = dr['title']
    dr['title'] = dr['url']
    dr = dr.drop(['keyword'], axis=1)
    dr = dr.drop(['url'], axis=1)
    dr.columns = ["id", "keyword", "url", "title"]
    dr['title'] = dr['keyword']
    dr.loc[dr.id >= 0, 'url'] = "https://" + dr.url
    dr.loc[dr.id >= 0, 'id'] = 1000 + dr.id
    dr.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c53.csv", index=None)

    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c53.csv")
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c54.csv")
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c54.csv")
    df.columns = ["num", "id", "keyword", "url", "title"]
    df.loc[df.id >= 0, 'num'] = 1000 + df.num
    df = df.drop(["id"], axis=1)
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c55.csv", index=None)
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c55.csv")
    df.columns = ["id", "keyword", "url", "title"]
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c56.csv", index=None)

    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c110.csv")
    df.columns = ["1", "2", "3", "4", "5"]
    df = df.dropna(axis=0, how='any')
    df = df.drop(["1"], axis=1)
    df = df.drop(["2"], axis=1)
    df = df.drop(["3"], axis=1)
    df = df.drop(["5"], axis=1)
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\uv111.csv", index=None)
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\uv111.csv")
    df.columns = ["name"]
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c112.csv", index=None)
    ft2 = r'\[|\]|\,|\''
    dt = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c56.csv")
    dr = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c112.csv")
    de = pd.concat([dt, dr], axis=1)
    de = pd.DataFrame(de)
    de.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c570.csv", index=None)
    dt = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c570.csv")
    dt['keyword'] = dt['name']
    dt = dt.drop(['name'], axis=1)
    dt.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c580.csv", index=None)
    dt = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c580.csv")
    dt['title'] = dt['keyword']
    dt['title'] = dt.apply(lambda x: re.sub(ft2, '', x['title']).strip(), axis=1)
    dt.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c590.csv", index=None)
    print("Finished")
    print("------------------------------------------------")
    print("Start building Chegg page index")
    print("------------------------------------------------")
    # 这一段是制作page_index
    ft3 = r'\[|\]|\,|\''
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c590.csv")
    df["title"] = df['title'].map(str.lower)
    df["keyword"] = df["keyword"] + df["title"]
    df["title"] = df['title'].map(str.upper)
    df["keyword"] = df["keyword"] + df["title"]
    df['keyword'] = df.apply(lambda x: re.sub(ft3, '', x['keyword']).strip(), axis=1)
    df = df.drop(["id"], axis=1)
    df = df.drop(["title"], axis=1)
    df = df.drop(["url"], axis=1)
    # ua_610与桌面上的999为同一个文件
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c610.csv", header=None)
    # 999到1117
    ft4 = r'\d\d\d'
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    with open(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c610.csv", encoding='utf8') as f:
        data = f.readlines()
        r = 1000
        for i in data:
            k = wordninja.split(i)
            i.replace('[', ' ')
            i.replace(']', ' ')
            i.replace("’", " ")
            i.replace("'", " ")
            for y in k:
                r = str(r)
                list2 = [r + l for l in k]
            list3.extend(list2)
            r = int(r)
            r = r + 1
        for q in list3:
            list4.append(q)
            s = q[0:]
            o = pd.DataFrame(list4)
            o.index.name = None
            o.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c611.csv", header=None,
                     index=None)
    ft5 = r'\d\d\d\d'
    df = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c611.csv")
    df['id'] = df.apply(lambda x: re.match(ft5, x["10000"]).group(), axis=1)
    df.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c612.csv", index=None)
    dk = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c612.csv")
    dk['10000'] = dk.replace(re.compile(ft5), '')
    dk['10000'] = dk.replace("'", "Nan")
    dk = dk[~dk['10000'].isin(['Nan'])]
    dk.reset_index()
    dk.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c613.csv", header=None)
    dr = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c613.csv")
    dr.columns = ["id", "keyword", "page_id"]
    dr.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c614.csv", index=None)
    dr = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c614.csv")
    dr = dr.drop(['id'], axis=1)
    dr.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c615.csv")
    dr = pd.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c615.csv")
    dr.columns = ["id", "keyword", "page_id"]
    dr.to_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c616.csv", index=None)
    print("Finished")
    print("Start trans data to database")
    print("------------------------------------------------")
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\amazon_info.db")
    df = pandas.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a590.csv")
    df.to_sql('page_info1', conn, if_exists='append', index=False)
    dk = pandas.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\amazon_price\u_a616.csv")
    dk.to_sql('page_index1', conn, if_exists='append', index=False)

    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\chegg_info.db")
    df = pandas.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c590.csv")
    df.to_sql('page_info2', conn, if_exists='append', index=False)
    dk = pandas.read_csv(r"C:\Users\Administrator\Desktop\python\pycharm1\CSV\chegg_info\u_c616.csv")
    dk.to_sql('page_index2', conn, if_exists='append', index=False)
    print("Finished")
    run(host='localhost', port=8080)