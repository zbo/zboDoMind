#!/usr/bin/python
# -*- coding:utf8 -*-

from selenium import webdriver


def webget(keyword):
    browser.get(url.format(keyword))
    top_bar = browser.find_elements_by_id('table_top_bar')
    num = top_bar[0].find_element_by_class_name('num')
    return num.text


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    url = 'http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=result_rewrite&selfsectsn=&querytype' \
          '=stock&searchfilter=&tid=stockpick&w={0} '
    browser = webdriver.Chrome(chrome_options=options)
    sz = webget('上涨')
    xd = webget('下跌')
    sz5 = webget('上涨大于5%')
    xd5 = webget('下跌大于5%')
    zt = webget('非st涨停')
    dt = webget('非st跌停')
    zb = webget('非st炸板')
    fb = webget('反包 昨日下跌大于3%')
    llb = webget('非st，非新股，两连板')
    slb = webget('非st，非新股，三连板')
    lb4 = webget('非st，非新股，四连板')
    lb5 = webget('非st，非新股，五连板')
    lb6 = webget('非st，非新股，六连板')
    lb7 = webget('非st，非新股，七连板以上')
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
