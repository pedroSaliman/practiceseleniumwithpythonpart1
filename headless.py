from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

ops=webdriver.ChromeOptions()
ops.headless=True
driver = webdriver.Chrome(ChromeDriverManager().install(),options=ops)

driver.get("https://opensource-demo.orangehrmlive.com/")




