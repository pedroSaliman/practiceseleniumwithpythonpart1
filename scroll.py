from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.nopcommerce.com/")
driver.execute_script("window.scrollBy(0,2000)")
driver.find_element(By.XPATH,"//a[normalize-space()='Contact us']").click()