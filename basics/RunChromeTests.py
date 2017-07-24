import os

from selenium import webdriver


class RunChromeTests():
    def test(self):

        driver_location = "/Users/GauravHansda/Documents/workspace/selenium/chromedriver"
        os.environ["webdriver.chrome.driver"] = driver_location
        # Instantiate FF browser command
        driver = webdriver.Chrome(driver_location)

        # Open the provided url
        driver.get("http://www.yahoo.com")


ff = RunChromeTests()
ff.test()
