from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

# 判断元素是否存在的函数
# def is_element_exist(clas):
#     s = driver.find_elements_by_class_name(clas)
#     if len(s) == 0:
#         return  False
#     else:
#         return  True


driver = webdriver.Chrome()
driver.get("http://t.cn/RmoVQ8t")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_id('telephone').send_keys('your telephone')
driver.find_element_by_id('btnGetVerifyCode').click()
verifycode = input("please input:")
driver.find_element_by_id('verifycode').send_keys(verifycode)
driver.find_element_by_id('loginSubmit').click()
time.sleep(5)
driver.find_element_by_class_name('btn_start_image').click()
time.sleep(5)

# 控制游戏局数
j = 20

while j > 0:

    e1 = driver.find_element_by_xpath("//*[@id='game_body']/div[6]")
    e2 = driver.find_element_by_xpath("//*[@id='game_body']/div[7]")
    e3 = driver.find_element_by_xpath("//*[@id='game_body']/div[10]")
    e4 = driver.find_element_by_xpath("//*[@id='game_body']/div[11]")

    i = True

    while  i:
        try:
            chain = ActionChains(driver)
            
#           上下左右拖动鼠标
            chain.drag_and_drop_by_offset(e1,0,-2).perform()
            # time.sleep(2)
            chain.drag_and_drop_by_offset(e2, -2, 0).perform()
            # time.sleep(2)
            chain.drag_and_drop_by_offset(e3, 0, 2).perform()
            # time.sleep(2)
            chain.drag_and_drop_by_offset(e4, 2, 0).perform()
            # time.sleep(2)
            time.sleep(0.5)
#             i += 1
#             print(i)
            
        except StaleElementReferenceException as msg:
            break

#            开启新局
    time.sleep(1)
    print('NEW GAME %d' % j)
    driver.find_element_by_id('btnReset').click()
    time.sleep(1)
    driver.find_element_by_class_name('btn_start_image').click()
    time.sleep(3)
    j -= 1

driver.quit()
