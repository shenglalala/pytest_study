from selenium import webdriver


class d_hless():

    def handless_driver(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--window-size=1920,1080')
        self.co_driver = webdriver.Chrome('chromedriver', options=self.chrome_options)
        return self.co_driver