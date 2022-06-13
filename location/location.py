from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

def getLocation():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    # options.add_argument("--headless")
    timeout = 1
    driver = webdriver.Chrome(executable_path = 'D:\Downloads\chromedriver_win32\chromedriver', chrome_options=options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(1)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()
    user_location = {
        'lat': latitude,
        'long': longitude
    }
    return (user_location)
print(getLocation())