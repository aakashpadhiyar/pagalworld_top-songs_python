
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

####>DOWNLOAD MUSIC FILES####
page = int(input('pages: '))
driver = webdriver.Chrome(executable_path='./chromedriver')
for i in range(page):
    driver.get('https://www.pagalworld.mobi/top-songs.html?page={}'.format(i+1))
    for i in range(25):
        listt = driver.find_elements_by_xpath("//div[@class='cat-list']")
        io = listt[i]
        io.click()
        music = driver.find_element_by_class_name('dbutton')
        music.click()
        sleep(1)
        driver.back()
