from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/")
cookie=driver.get_cookies()
print(cookie)
size=len(cookie)
print(size)
driver.add_cookie({"name":"orangehrm","value":"123456789"})
print(cookie)
