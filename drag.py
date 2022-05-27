from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
src=driver.find_element(By.XPATH,"//div[@id='column-a']")
trget=driver.find_element(By.XPATH,"//div[@id='column-b']")
act=ActionChains(driver)
act.drag_and_drop(src,trget)