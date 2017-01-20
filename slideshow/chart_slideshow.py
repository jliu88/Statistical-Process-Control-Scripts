#!usrs/bin/env python

import os
from shutil import copyfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

miseqruo_dir = r'\\ushw-file\users\transfer\Hayward_Statistical_Process_Control\Control_Charts\MiSeq\OP750\MiSeqRUO'
backup_dir = r'\\ushw-file\depts\Ops\MFG\iMFG\ReleaseTest\MiSeq_Data\Jimmy\SPC Scripts\Beta\Screen Display\Backup Charts'

chart_list = []      

#Initialize 
driver = webdriver.Ie()
#driver.get('https://google.com')
#driver.find_element_by_tag_name('body').send_keys(Keys.F11)

i = 0

while i != -1:
    #Tries to access network location to backup files, if cannot then use the
    #original backup files
    try:
        for files in os.listdir(miseqruo_dir):
            #If files ends with .svg then copy the files onto a backup location 
            #and add the file name to a list
            if files.endswith('.svg'):
                backup = os.path.join(backup_dir, files)
                copyfile(os.path.join(miseqruo_dir, files), backup)
                chart_list.append(os.path.join(backup_dir, files))
    except Exception:
        pass
    for chart in chart_list:
        driver.get(chart)
        sleep(5)





