from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/context_menu")
right=driver.find_element(By.XPATH,"//div[@id='hot-spot']")
act=ActionChains(driver)
act.context_click(right)