#!/usr/bin/python
# -*- coding:utf8 -*-

from selenium import webdriver
import readconf

def webget(keyword):
    browser.get(url.format(keyword))
    top_bar = browser.find_elements_by_id('table_top_bar')
    num = top_bar[0].find_element_by_class_name('num')
    return num.text


def score(cond):
    if cond:
        return 2
    else:
        return -2

dic = readconf.read()
jrday = dic['jrday']
zrday = dic['zrday']
qrday = dic['qrday']

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    url = 'http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=result_rewrite&selfsectsn=&querytype' \
          '=stock&searchfilter=&tid=stockpick&w={0} '
    browser = webdriver.Chrome(chrome_options=options)
    ret_list = []
    # 涨停板数量 大于 50 +2分
    ztsl = int(webget('非st，非新股，{0}涨停'.format(jrday)))
    ztsl_score = score(ztsl > 50)
    print "[涨停多] 涨停板数量大于50:{0} 得分{1}".format(ztsl, ztsl_score)
    # 连续涨停板数量 大于 10 +2分
    lxztsl = int(webget('非st，非新股，{0}涨停，{1}涨停'.format(zrday,jrday)))
    lxztsl_score = score(lxztsl > 10)
    print "[连板多] 连续涨停板数量大于10:{0} 得分{1}".format(lxztsl, lxztsl_score)
    # 跌幅大于5%不包含跌停 小于 100 +2分
    xd5 = int(webget('非st，非新股，跌幅大于5%不包含跌停'))
    xd5_score = score(xd5 < 100)
    print "[大面少] 跌幅大于5%不包含跌停数量小于100:{0} 得分{1}".format(xd5, xd5_score)
    # 红盘个数比 大于一半 +2分
    sz = int(webget('上涨'))
    xd = int(webget('下跌'))
    hp_score = score(sz > xd)
    print "[涨多跌少] 上涨数量:{0} 下跌数量:{1} 得分{2}".format(sz, xd, hp_score)
    # 下跌5%和涨停比较得分 3<1 +2分
    str_score = score(ztsl > xd5)
    print "[31关系] 涨停数量:{0} 下跌5%数量:{1} 得分{2}".format(ztsl, xd5, str_score)
    print "---------------"
    print "惯性势能{0}".format(ztsl_score + lxztsl_score + xd5_score + hp_score + str_score)
    print "---------------"