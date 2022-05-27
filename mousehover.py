from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/hovers")
hover=driver.find_element(By.XPATH,"//div[@class='example']//div[1]//img[1]")
act= ActionChains(driver)
act.move_to_element(hover).perform()