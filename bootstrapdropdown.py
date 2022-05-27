from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.CSS_SELECTOR,"#select2-billing_country-container").click()
driver.implicitly_wait(10)

countrylist = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countrylist))

for country in countrylist:
    if country == "Egypt":
        country.click()
        break
