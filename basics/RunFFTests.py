from selenium import webdriver

class RunFFTests():
    def test(self):
        # Instantiate FF browser command
        driver = webdriver.Firefox()

        #Open the provided url
        driver.get("http://www.letskodeit.com")

ff = RunFFTests()
ff.test()
