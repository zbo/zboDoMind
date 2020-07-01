#!/usr/bin/python
# -*- coding:utf8 -*-

from selenium import webdriver
import readconf


def webget(keyword):
    browser.get(url.format(keyword))
    top_bar = browser.find_elements_by_id('table_top_bar')
    num = top_bar[0].find_element_by_class_name('num')
    return num.text


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    dic = readconf.read()
    jrday = dic['jrday']
    zrday = dic['zrday']
    qrday = dic['qrday']

    url = 'http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=result_rewrite&selfsectsn=&querytype' \
          '=stock&searchfilter=&tid=stockpick&w={0} '
    browser = webdriver.Chrome(chrome_options=options)
    sz = webget('{0}上涨'.format(jrday))
    xd = webget('{0}下跌'.format(jrday))
    print '上涨:{sz} 下跌:{xd}'.format(sz=sz, xd=xd)
    sz5 = webget('{0}上涨大于5%'.format(jrday))
    xd5 = webget('{0}下跌大于5%'.format(jrday))
    print '上涨大于5%:{sz5} 下跌大于5%:{xd5}'.format(sz5=sz5, xd5=xd5)
    llb = webget('非st,非新股,{0},两连板'.format(jrday))
    slb = webget('非st,非新股,{0},三连板'.format(jrday))
    lb4 = webget('非st,非新股,{0},四连板'.format(jrday))
    lb5 = webget('非st,非新股,{0},五连板'.format(jrday))
    lb6 = webget('非st,非新股,{0},六连板'.format(jrday))
    lb7 = webget('非st,非新股,{0},七连板以上'.format(jrday))
    print '两连板:{llb} 三连板:{slb}'.format(llb=llb, slb=slb)
    print '四连板:{0} 五连板:{1} 六连板:{2} 七连板以上:{3}'.format(lb4,lb5,lb6,lb7)
    print '----------------'
    zt = webget('非st,{0}涨停'.format(jrday))
    dt = webget('非st,{0}跌停'.format(jrday))
    zb = webget('非st,{0}炸板'.format(jrday))
    print '[失败可能-涨停炸板比300%+]涨停:{zt} 跌停:{dt} 炸板:{zb}'.format(zt=zt, dt=dt, zb=zb)
    
    zrzb = webget('非st,{0}炸板'.format(zrday))
    jrsz = webget('非st,{0}炸板,{1}上涨'.format(zrday, jrday))
    jrjt = webget('非st,{0}炸板,{1}最高价大于{2}最高价'.format(zrday, jrday, zrday))
    print '[失败代价-昨日解套50%+]昨日炸板{0},今日上涨{1},昨日炸板今日解套{2}'.format(zrzb,jrsz,jrjt)
    
    print '-------------------------------------'
    print '动能势能定开仓，黄白线定盘口'
    print '炸板涨停定打板或低吸，龙头位差定梯队'
    print '-------------------------------------'
