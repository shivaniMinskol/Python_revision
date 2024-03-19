import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# drop_down:-
driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

ele=driver.find_element(By.TAG_NAME,"select")
drd=Select(ele)
drd.select_by_value("IND")
time.sleep(5)

# -----------------------------------------------------------------

