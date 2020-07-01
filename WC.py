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
    print '上涨大于5%:{sz5} 下跌大于5%:{xd5} \n'.format(sz5=sz5, xd5=xd5)
    zt = webget('非st,{0}涨停'.format(jrday))
    dt = webget('非st,{0}跌停'.format(jrday))
    print '涨停:{zt} 跌停:{dt}'.format(zt=zt, dt=dt)
    zb = webget('非st,{0}炸板'.format(jrday))
    fb = webget('反包, {0}下跌大于3%'.format(zrday))
    print '今日反包:{fb} 今日炸板:{zb}'.format(fb=fb, zb=zb)
    zrzb = webget('非st,{0}炸板'.format(zrday))
    jrsz = webget('非st,{0}炸板,{1}上涨'.format(zrday, jrday))
    print '昨日炸板{0},今日上涨{1}'.format(zrzb,jrsz)
    llb = webget('非st,非新股,{0},两连板'.format(jrday))
    slb = webget('非st,非新股,{0},三连板'.format(jrday))
    lb4 = webget('非st,非新股,{0},四连板'.format(jrday))
    lb5 = webget('非st,非新股,{0},五连板'.format(jrday))
    lb6 = webget('非st,非新股,{0},六连板'.format(jrday))
    lb7 = webget('非st,非新股,{0},七连板以上'.format(jrday))         
    print '两连板:{llb} 三连板:{slb}'.format(llb=llb, slb=slb)
    print '四连板:{0} 五连板:{1} 六连板:{2} 七连板以上:{3}'.format(lb4,lb5,lb6,lb7)
    
