# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time
import undetected_chromedriver
from selenium.webdriver.common.by import By
from decouple import config

# options = webdriver.ChromeOptions()
# options.add_argument("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36")
# options.add_argument("--disable-blink-features=AutomationControlled")

# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s, options=options)
driver = undetected_chromedriver.Chrome()

try:
    driver.get("https://www.olx.ua/uk/")
    time.sleep(1)

    email = config('EMAIL')
    password = config('PASSWORD')

    klick_registration = driver.find_element(By.LINK_TEXT, "Ваш профіль").click()
    time.sleep(5)

    
    email_input = driver.find_element(By.NAME, 'username')
    email_input.clear()
    email_input.send_keys(email)
    time.sleep(1)

    paswword_input = driver.find_element(By.NAME, 'password')
    paswword_input.clear()
    paswword_input.send_keys(password)
    time.sleep(1)

    login_button = driver.find_element(By.CSS_SELECTOR, 'button.css-ypypxs').click()
    time.sleep(20)

    img_olx = driver.find_element(By.CSS_SELECTOR, 'span.css-1kpgv52').click()
    time.sleep(2)

    



except Exception as ex:
    print(ex)    
finally:
    driver.close()
    driver.quit()
