#!/usr/bin/python
# -*- coding:utf8 -*-

from selenium import webdriver
import readconf
import sys


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
    #1 昨日涨停今日红盘比 大于 0.6 +2分
    zrzt = int(webget("非st,非新股,{0}涨停".format(zrday)))
    zrzt_hp = int(webget("非st,非新股,{0}涨停, {1}上涨".format(zrday,jrday)))
    score1 = score(zrzt * 0.6 < zrzt_hp)
    print "[昨日涨停上涨60%+] 昨日涨停:{0} 今天上涨:{1} 占比{2}% 得分:{3}".format(zrzt, zrzt_hp, zrzt_hp*100/zrzt, score1)

    #2 昨日涨停今日跌幅超5%比例 小于 0.3 +2分
    zrzt_dm = int(webget("非st,非新股,{0}涨停, {1}跌幅大于5%".format(zrday,jrday)))
    score2 = score(zrzt_dm < zrzt*0.3)
    print "[昨日涨停大面30%-] 昨日涨停:{0} 今天大面:{1} 占比{2}% 得分:{3}".format(zrzt, zrzt_dm, zrzt_dm*100/zrzt, score2)

    #3 昨日连续涨停今日红盘比 大于 0.6 +2分
    zrlxzt = int(webget("非st,非新股, {0}涨停, {1}涨停".format(zrday,qrday)))
    zrlxzt_hp = int(webget("非st,非新股, {0}涨停, {1}涨停, {2}上涨".format(zrday,qrday,jrday)))
    score3 = score(zrlxzt * 0.6 < zrlxzt_hp)
    print "[昨日连板上涨60%+] 昨日连板:{0} 今天上涨:{1} 占比{2}% 得分:{3}".format(zrlxzt, zrlxzt_hp, zrlxzt_hp*100/zrlxzt, score3)

    #4 昨日连板涨停今日跌幅超5%比例 小于 0.3 +2分
    zrlxzt_dm = int(webget("非st, 非新股, {0}涨停, {1}涨停, {2}跌幅大于5%".format(qrday,zrday,jrday)))
    score4 = score(zrlxzt_dm < zrlxzt * 0.3)
    print "[昨日连板大面30%-] 昨日连续涨停:{0} 今天大面:{1} 占比{2}% 得分:{3}".format(zrlxzt, zrlxzt_dm, zrlxzt_dm*100/zrlxzt, score4)

    #5 今日连板数和昨日连板数 大于 0.8 +2分
    jrlxzt = int(webget("非st, 非新股, {0}涨停, {1}涨停".format(zrday,jrday)))
    score5 = score(jrlxzt>zrlxzt*0.8)
    print "[今日连板昨日连板80%+] 今日连板{0} 昨日连板{1} 比例{2}% 得分{3}".format(jrlxzt,zrlxzt,jrlxzt*100/zrlxzt,score5)

    #6 昨日断板绿盘比例 小于 0.5 +2分
    lp = int(webget("非st,非新股,{0}未能涨停, {1}连板".format(zrday,qrday)))
    lp2 = int(webget("非st,非新股,{0}未能涨停,{1}连板, {2}下跌".format(zrday,qrday,jrday)))
    score6 = score(lp2 < lp * 0.5)
    print "[昨日断板下跌50%-] 昨日断板:{0} 断板后今天下跌:{1} 占比{2}% 得分:{3}".format(lp, lp2, lp2*100/lp, score6)


    print "---------------"
    print "燃料动能{0}".format(score1 + score2 + score3 + score4 + score5 + score6)
    print "---------------"

    # 其他
    # 今日炸板和涨停比 小于 30% +2分
    # zb = int(webget("非st,非新股,今日炸板"))
    # zt = int(webget("非st,非新股,今日涨停"))
    # print "[今日炸板] 炸板:{0} 涨停:{1} 得分:--".format(zb,zt)
    # zbdm = int(webget("非st,非新股,{0}炸板,今日下跌超过4%".format(zrday)))
    # zbsz = int(webget("非st,非新股,{0}炸板,今日上涨".format(zrday)))
    # print "[昨日炸板大面比] 昨日炸板{0} 今日上涨{1} 占比{2}% 大面{3} 占比{4}%".format(zb,zbsz, zbsz*100/zb, zbdm, zbdm*100/zb)
    # gn_list = ["头条概念","室外经济概念","免税概念","芯片概念","网络游戏概念","特斯拉概念","证券板块"]
    # gndm_tmp = "非st,非新股,今日跌幅大于4%, {0}"
    # gndz_tmp = "非st,非新股,今日涨幅大于4%, {0}"
    # best = 0
    # best_g = ""
    # for g in gn_list:
    #     gn = int(webget(g))
    #     gndm = int(webget(gndm_tmp.format(g)))
    #     gndz = int(webget(gndz_tmp.format(g)))
    #     dz_percentage = gndz*100/gn
    #     dm_percentage = gndm*100/gn
    #     if dz_percentage>best:
    #         best = dz_percentage
    #         best_g = g
    #     print "[{0}]总量{1} 大涨{2} 占比{3}% 大面{4} 占比{5}%".format(g,gn,gndz,dz_percentage,gndm,dm_percentage)
    # print "---------------"
    # print "最强板块{0}".format(best_g)
    # print "---------------"
