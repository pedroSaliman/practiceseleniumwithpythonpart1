from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.nopcommerce.com/")
ele=driver.find_element(By.XPATH,"//a[normalize-space()='Contact us']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
