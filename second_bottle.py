import sqlite3
import wordninja
from bottle import route, run, template, request, static_file, redirect
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
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\test1.db")
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
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\test1.db")
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
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\test2.db")
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
    conn = sqlite3.connect(r"C:\Users\Administrator\Desktop\test2.db")
    c = conn.cursor()
    sql = "select page_id " \
          + "from page_index2  " \
          + "where keyword in " + keyword + ";"
    res = c.execute(sql)
    res = [r[0] for r in res]
    return res

if __name__ == '__main__':
    run(host='localhost', port=8080)

