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
    sz5 = webget('{0}上涨大于5%'.format(jrday))
    xd5 = webget('{0}下跌大于5%'.format(jrday))
    zt = webget('非st,{0}涨停'.format(jrday))
    dt = webget('非st,{0}跌停'.format(jrday))
    zb = webget('非st,{0}炸板'.format(jrday))
    fb = webget('反包, {0}下跌大于3%'.format(jrday))
    llb = webget('非st,非新股,{0},两连板'.format(jrday))
    slb = webget('非st,非新股,{0},三连板'.format(jrday))
    lb4 = webget('非st,非新股,{0},四连板'.format(jrday))
    lb5 = webget('非st,非新股,{0},五连板'.format(jrday))
    lb6 = webget('非st,非新股,{0},六连板'.format(jrday))
    lb7 = webget('非st,非新股,{0},七连板以上'.format(jrday))
    ret_list = ['上涨:{sz} 下跌:{xd} \n'.format(sz=sz, xd=xd),
                '上涨大于5%:{sz5} 下跌大于5%:{xd5} \n'.format(sz5=sz5, xd5=xd5),
                '涨停:{zt} 跌停:{dt} \n'.format(zt=zt, dt=dt),
                '反包:{fb} 炸板:{zb} \n'.format(fb=fb, zb=zb),
                '两连板:{llb} 三连板:{slb} \n'.format(llb=llb, slb=slb),
                '四连板:{0} 五连板:{1} 六连板:{2} 七连板以上:{3}\n'.format(lb4,lb5,lb6,lb7)]
    content = "".join(ret_list)
    file_object = open('today.log', 'w')
    file_object.writelines(content)
    file_object.close()
