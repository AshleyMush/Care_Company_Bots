class BirdieBot():
    def __init__(self, email, fname, lName,phone, teamName,position):
        self.contact_time = "09:00-18:00"
        self.org = "Angel Care Group Ltd"
        self.phone = "07861389649"

        self.email = email
        self.password = password
        self.birdie_url = BIRDIE_URL
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

        """
        self.list_of_windows = len(self.driver.window_handles)
        self.base_window = self.driver.window_handles[0]
        """