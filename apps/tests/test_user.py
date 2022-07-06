from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains

from flask import url_for
from flask_testing import LiveServerTestCase

from .. import app
from .. import models


class TestUserTakesTheTest(LiveServerTestCase):

    def create_app(self):
        app.config.from_object('apps.tests.config')
        return app

    def setUp(self):

        USER_ID = app.config['FB_USER_ID']
        USER_NAME = app.config['FB_USER_NAME']
        USER_GENDER = app.config['FB_USER_GENDER']

        self.driver = webdriver.Chromium()
        models.init_db()

        self.result_page = url_for(
            'result',
            id=USER_ID,
            gender=USER_GENDER,
            first_name=USER_NAME,
            _external=True
        )
        self.wait = ui.WebDriverWait(self.driver, 1000)

    def tearDown(self):
        self.driver.quit()

    def getElement(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def enterTextField(self, selector, text):
        text_field = self.getElement(selector)
        text_field.clear()
        text_field.send_keys(text)

    def submitsForm(self):
        USER_EMAIL = app.config['FB_USER_EMAIL']
        USER_PASSWORD = app.config['FB_USER_PW']
        BTN_LOGIN = '#loginbutton input[name=login]'

        self.enterTextField('#email', USER_EMAIL)
        self.enterTextField('#pass', USER_PASSWORD)
        self.getElement(BTN_LOGIN).click()

    def seesLoginPage(self):
        LOGIN_URL = 'https://www.facebook.com/login.php'
        self.wait.until(lambda driver: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(lambda driver: self.get_el('#email'))
        assert self.driver.current_url.startswith(LOGIN_URL)

    def clicksOnLogin(self):
        button = self.getElement(".fb-login-button")
        iframe = lambda driver: self.driver.find_element_by_tag_name("iframe").is_displayed()
        self.wait.until(iframe)
        ActionChains(self.driver).click(button).perform()

    def testUserLogin(self):
        self.driver.get(self.get_server_url())
        self.clicksOnLogin()
        self.seesLoginPage()
        self.submitsForm()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.wait.until(lambda driver: '?' in self.driver.current_url)
        assert self.driver.current_url == self.result_page
