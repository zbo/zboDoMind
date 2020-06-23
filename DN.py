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

zrday = "周一"
qrday = "周五"

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    url = 'http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=result_rewrite&selfsectsn=&querytype' \
          '=stock&searchfilter=&tid=stockpick&w={0} '
    browser = webdriver.Chrome(chrome_options=options)
    ret_list = []
    # 昨日涨停今日红盘比 大于 0.6 +2分
    zrzt = int(webget("非st，非新股，{0}涨停".format(zrday)))
    zrzt_hp = int(webget("非st，非新股，{0}涨停, 今日上涨".format(zrday)))
    score1 = score(zrzt * 0.6 < zrzt_hp)
    print "[昨日涨停上涨60%+] 昨日涨停:{0} 今天上涨:{1} 占比{2}% 得分:{3}".format(zrzt, zrzt_hp, zrzt_hp*100/zrzt, score1)

    # 昨日连续涨停今日红盘比 大于 0.6 +2分
    zrlxzt = int(webget("非st，非新股，{0}连板".format(zrday)))
    zrlxzt_hp = int(webget("非st，非新股，{0}连板, 今日上涨".format(zrday)))
    score2 = score(zrlxzt * 0.6 < zrlxzt_hp)
    print "[昨日连板上涨60%+] 昨日连板:{0} 今天上涨:{1} 占比{2}% 得分:{3}".format(zrlxzt, zrlxzt_hp, zrlxzt_hp*100/zrlxzt, score2)

    # 昨日断板绿盘比例 小于 0.4 +2分
    lp = int(webget("非st，非新股，{0}未能涨停，{1}涨停".format(zrday,qrday)))
    lp2 = int(webget("非st，非新股，{0}未能涨停，{1}涨停， 今天下跌".format(zrday,qrday)))
    score5 = score(lp2 < lp * 0.4)
    print "[昨日断板下跌] 昨日断板:{0} 断板后今天下跌:{1} 占比{2}% 得分:{3}".format(lp, lp2, lp2*100/lp, score5)

    # 昨日涨停今日跌幅超4%比例 小于 0.4 +2分
    zrzt_dm = int(webget("非st，非新股，{0}涨停, 今日跌幅大于4%".format(zrday)))
    score3 = score(zrzt_dm < zrzt*0.4)
    print "[昨日涨停大面] 昨日涨停:{0} 今天大面:{1} 占比{2}% 得分:{3}".format(zrzt, zrzt_dm, zrzt_dm*100/zrzt, score3)

    # 昨日连板涨停今日跌幅超4%比例 小于 0.4 +2分
    zrlxzt_dm = int(webget("非st，非新股，{0}连板, 今日跌幅大于4%".format(zrday)))
    score4 = score(zrlxzt_dm < zrlxzt * 0.4)
    print "[昨日连板大面] 昨日连续涨停:{0} 今天大面:{1} 占比{2}% 得分:{3}".format(zrlxzt, zrlxzt_dm, zrlxzt_dm*100/zrlxzt, score4)

    # 今日炸板和涨停比 小于 30% +2分
    zb = int(webget("非st，非新股，今日炸板"))
    zt = int(webget("非st，非新股，今日涨停"))
    score6 = score(zb < zt*0.3)
    print "[今日炸板] 炸板:{0} 涨停:{1} 得分:{2}".format(zb,zt,score6)
    print "---------------"
    print "燃料动能{0}".format(score1 + score2 + score3 + score4 + score5 + score6)
    print "---------------"

    # 其他
    zbdm = int(webget("非st，非新股，{0}炸板，今日下跌超过4%".format(zrday)))
    zbsz = int(webget("非st，非新股，{0}炸板，今日上涨".format(zrday)))
    print "[昨日炸板大面比] 昨日炸板{0} 今日上涨{1} 占比{2}% 大面{3} 占比{4}%".format(zb,zbsz, zbsz*100/zb, zbdm, zbdm*100/zb)

    gn_list = ["头条概念","室外经济概念","免税概念","芯片概念","网络游戏概念","特斯拉概念"]
    gndm_tmp = "非st，非新股，今日跌幅大于4%, {0}"
    gndz_tmp = "非st，非新股，今日涨幅大于4%, {0}"
    for g in gn_list:
        gn = int(webget(g))
        gndm = int(webget(gndm_tmp.format(g)))
        gndz = int(webget(gndz_tmp.format(g)))
        print "[{0}]总量{1} 大涨{2} 占比{3}% 大面{4} 占比{5}%".format(g,gn,gndz,gndz*100/gn,gndm,gndm*100/gn)