from selenium import webdriver

class WebDriverFactory():
    """
    create a webdriver instannce and return web driver based on the browser config
    ##Note##
    Executable path for the webdriver should pointed to the environment variables in your system default
    """
    def __init__(self, browser):
        self.browser = browser
    def getDriverInstance(self):
        baseUrl = "https://letskodeit.com/"
        if self.browser == "chrome":
            chrome_opt = webdriver.ChromeOptions()
            chrome_opt.add_argument("--disable-gpu")
            driver = webdriver.Chrome(options= chrome_opt)
            #set maximum size based on system resolution usage
            driver.set_window_size(1366,768)
        elif self.browser == "firefox":
            driver = webdriver.Firefox
        elif self.browser == "ie":
            driver = webdriver.Ie
        elif self.browser == "safari":
            driver = webdriver.Safari
        #maximize the window
        driver.maximize_window()
        driver.implicitly_wait(8)
        #navigate browser window to the mentioned base url
        driver.get(baseUrl)
        return driver


