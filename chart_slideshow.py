#!usrs/bin/env python

import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

miseqruo_dir = r'\\ushw-file\users\transfer\Hayward_Statistical_Process_Control\Control_Charts\MiSeq\OP750\MiSeqRUO'

chart_list = []

for files in os.listdir(miseqruo_dir):
    if files.endswith('.svg'):
        chart_list.append(files)


loop_list = [os.path.join(miseqruo_dir, entry) for entry in chart_list]

#Initialize 
driver = webdriver.Ie()
driver.get('https://google.com')
driver.find_element_by_tag_name('body').send_keys(Keys.F11)

i = 0

while i != -1:
    for chart in loop_list:
        driver.get(chart)
        sleep(5)





