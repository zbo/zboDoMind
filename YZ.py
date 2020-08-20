from selenium import webdriver
import readconf
from datetime import datetime

def webget(keyword):
    browser.get(url.format(keyword))
    top_bar = browser.find_elements_by_id('table_top_bar')
    num = top_bar[0].find_element_by_class_name('num')
    return num.text
dic = readconf.read()
yzdays = dic['yzdays']

if __name__ == '__main__':
    alldays = yzdays.split(',')
    for day in alldays:
        keyword = "2020{day}".format(day=day)
        print keyword
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    url = 'https://www.lhbjd.com/lhb/day/20200820/'
    browser = webdriver.Chrome(chrome_options=options)
    