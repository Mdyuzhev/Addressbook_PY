from selenium import webdriver


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("group page").click()

    def create_group(self, group):
        driver = self.driver
        self.open_groups_page()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def login(self, username, password):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
