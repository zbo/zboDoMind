#!/usr/bin/python
# -*- coding:utf8 -*-

from selenium import webdriver
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

watch_list = ['省广集团', '双林股份', '久其软件', '上证指数']


def webget(keyword):
    browser.get(url.format(keyword))
    top_bar = browser.find_elements_by_id('doctorPick')
    name = top_bar[0].find_element_by_class_name('pickName')
    price = top_bar[0].find_element_by_class_name('pick_price')
    zd = top_bar[0].find_element_by_class_name('pick_zd_zdf')
    return "{0} {1} {2}\n".format(name.text, price.text, zd.text)


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=options)
    ret_list = []
    url = 'http://www.iwencai.com/stockpick/search?typed=1&preParams=&ts=1&f=1&qs=result_rewrite&selfsectsn=&querytype' \
          '=stock&searchfilter=&tid=stockpick&w={0} '
    for item in watch_list:
        ret = webget(item)
        ret_list.append(ret)
    content = "".join(ret_list)
    file_object = open('list.log', 'w')
    file_object.writelines(content)
    file_object.close()
    print content
