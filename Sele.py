from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome(r'C:\Users\a875714\Documents\chromedriver_win32\chromedriver')
driver.maximize_window()
driver.get('https://academybugs.com/find-bugs/')

#bug 1
def bug1():
    main_page = driver.current_window_handle
    ele = driver.find_element(By.XPATH, '//*[@id="ec_product_page"]/div[1]/span[1]/a[3]')
    ele.click()
    time.sleep(9)
    ele = driver.find_element(By.XPATH, '//*[@id="popmake-4406"]/button')
    ele.click()
    '''for handle in driver.window_handles:
        if handle != main_page:
            actual = handle
    driver.switch_to.window(actual) '''
    driver.get('https://academybugs.com/find-bugs/')
    #ele = driver.find_element(By.XPATH, '//*[@id="popmake-4393"]/button')
    #ele.click()

#bug2
def bug2():
    ele = driver.find_element(By.XPATH, '//*[@id="ec_product_image_effect_dark-grey-jeans"]/a')
    ele.click()
    ele = driver.find_element(By.XPATH, '//*[@id="popmake-4406"]/button')
    ele.click()

#bug3
def bug3():
    ele = driver.find_element(By.CSS_SELECTOR, '#post-1673 > div > section > div.ec_details_content > div.ec_details_right > form > div.ec_details_description.academy-bug')
    ele.click()

#bug4
def bug4():
    ele = driver.find_element(By.XPATH, '//*[@id="ec_product_image_effect_dark-grey-jeans"]/a')
    ele.click()
    ele = driver.find_element(By.XPATH, '//*[@id="ec_currency_conversion"]')
    ele.click()
    ele = driver.find_element(By.XPATH, '//*[@id="currency"]/input[1]')
    ele.click()

#bug5
def bug5():
    ele = driver.find_element(By.XPATH, '//*[@id="ec_product_image_effect_dark-grey-jeans"]/a')
    ele.click()
    ele = driver.find_element(By.XPATH, '//*[@id="post-1673"]/div/section/div[1]/div[3]/div[2]/div[2]/a/img')
    ele.click()

#bug6
def bug6():
    ele = driver.find_element(By.XPATH, '//*[@id="ec_product_image_effect_dark-grey-jeans"]/a')
    ele.click()
    ele = driver.find_element(By.ID, 'Comment')
    ele.send_keys('etc... running up that hill')
    ele = driver.find_element(By.ID, 'author')
    ele.send_keys('Diego')
    ele = driver.find_element(By.ID, 'email')
    ele.send_keys(r'a@a.com')
    ele = driver.find_element(By.ID, 'url')
    ele.send_keys('a.com')
    ele = driver.find_element(By.XPATH, '//*[@id="academy-comment-submit"]')
    ele.submit

#bug7
def bug7():
    ele = driver.find_element(By.XPATH, '//*[@id="ec_product_image_dark-blue-denim-jeans"]/div[3]/div[1]/span/a')
    ele.click()
    ele = driver.find_element(By.XPATH, '//*[@id="post-1375"]/div/div[2]/div[2]')
    ele.click()


bug1()
bug2()
bug3()
