# -*- coding:utf8 -*-
from selenium import webdriver
import readconf
from datetime import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def webget(keyword):
    url = 'https://www.lhbjd.com/lhb/day/{0}'.format(keyword)
    alllist = []
    browser.get(url)
    tables = browser.find_elements_by_class_name('table-dark')
    for table in tables:
        thead = table.find_element_by_tag_name('thead')
        youzi = thead.find_element_by_tag_name('a').text
        tbody = table.find_element_by_tag_name('tbody')
        trs = tbody.find_elements_by_tag_name('tr')
        for tr in trs:
            tds = tr.find_elements_by_tag_name('td')
            if len(tds) == 0:
                continue
            yinyebu = tds[0].text
            gupiao = tds[1].find_element_by_tag_name('a').text
            buy = 0
            if tds[2].text != '-':
                buy = float(tds[2].text)
            sell = 0
            if tds[3].text != '-':
                sell = float(tds[3].text)
            info = "{0},{1},{2},{3},{4},{5}\n".format(keyword,youzi,yinyebu,gupiao,buy,sell)
            alllist.append(info)
    return alllist
dic = readconf.read()
yzdays = dic['yzdays']

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=options)
    alldays = yzdays.split(',')
    for day in alldays:
        keyword = "2020{day}".format(day=day)
        print "procee {0}".format(keyword)
        list = webget(keyword)
        file_object = open('yz.csv', 'w')
        file_object.writelines("".join(list))
        file_object.close()
    
    