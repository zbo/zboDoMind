#!/usr/bin/python
# -*- coding:utf8 -*-

from selenium import webdriver
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


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


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    url = 'http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=result_rewrite&selfsectsn=&querytype' \
          '=stock&searchfilter=&tid=stockpick&w={0} '
    browser = webdriver.Chrome(chrome_options=options)
    ret_list = []
    # 昨日涨停今日红盘比 大于 0.6 +2分
    zrzt = int(webget("非st，周四涨停"))
    zrzt_hp = int(webget("非st，周四涨停, 今日上涨"))
    score1 = score(zrzt * 0.6 < zrzt_hp)
    print "[昨日涨停上涨60%+] 昨日涨停:{0} 今天上涨:{1} 得分:{2}".format(zrzt, zrzt_hp, score1)

    # 昨日连续涨停今日红盘比 大于 0.6 +2分
    zrlxzt = int(webget("非st，周四连板"))
    zrlxzt_hp = int(webget("非st，周四连板, 今日上涨"))
    score2 = score(zrlxzt * 0.6 < zrlxzt_hp)
    print "[昨日连板上涨60%+] 昨日连续涨停:{0} 今天上涨:{1} 得分:{2}".format(zrlxzt, zrlxzt_hp, score2)

    # 昨日涨停今日跌幅超4%比例 小于 0.3 +2分
    zrzt_dm = int(webget("非st，周四涨停, 今日跌幅大于4%"))
    score3 = score(zrzt_dm < zrzt*0.3)
    print "[昨日涨停大面30%-] 昨日涨停:{0} 今天大面:{1} 得分:{2}".format(zrzt, zrzt_dm, score3)

    # 昨日连板涨停今日跌幅超4%比例 小于 0.3 +2分
    zrlxzt_dm = int(webget("非st，周四连板, 今日跌幅大于4%"))
    score4 = score(zrlxzt_dm < zrlxzt * 0.3)
    print "[昨日连板大面30%-]昨日连续涨停:{0} 今天大面:{1} 得分:{2}".format(zrlxzt, zrlxzt_dm, score4)

    # 昨日断板绿盘比例 小于 0.4 +2分
    lp = int(webget("非st，周四未能涨停，周三涨停"))
    lp2 = int(webget("非st，周四未能涨停，周三涨停, 今天下跌"))
    score5 = score(lp2 < lp * 0.4)
    print "[昨日断板下跌40%-] 昨日断板:{0} 断板后今天下跌:{1} 得分:{2}".format(lp, lp2, score5)

    # 今日炸板和涨停比 小于 1/3 +2分
    zb = int(webget("非st，今日炸板"))
    zt = int(webget("非st，今日涨停"))
    score6 = score(zb*3 < zt)
    print "[今日炸板30%-]炸板:{0} 涨停:{1} 得分:{2}".format(zb,zt,score6)
    print "---------------"
    print "燃料动能{0}".format(score1 + score2 + score3 + score4 + score5 + score6)
     print "---------------"