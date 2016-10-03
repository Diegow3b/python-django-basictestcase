# -*- coding: utf-8 -*-
from django.test import TestCase

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from myApp.models import myModel
from django.core.exceptions import ValidationError
from splinter import Browser

# Create your tests here.
class ExemploViewsCaseTests(StaticLiveServerTestCase):
    '''
    Uma forma de chamar este teste diretamente:
        python manage.py test myApp.tests.model_tests.ExemploViewsCaseTests
    '''
    # python manage.py test pedido.tests.test_models.ExemploViewsCaseTests

    # E2E Tests
    @classmethod
    def setUpClass(cls):
        super(ExemploViewsCaseTests, cls).setUpClass()
        executable_path = {'executable_path':'/usr/bin/google-chrome'}
        cls.browser = Browser('chrome', **executable_path)
        # cls.browser = Browser('phantomjs')
        cls.browser.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(ExemploViewsCaseTests, cls).tearDownClass()

    def setUp(self):
        super(ExemploViewsCaseTests, self).setUp()
        self.username = "admin"
        self.password = "admin123"
        self.user = User.objects.create_superuser(username=self.username,
                                                  password=self.password,
                                                  email="email@email.com")
    def login(self, url_create):
        """
        :type url_create: String
        """
        self.browser.visit(self.live_server_url + url_create)
        self.browser.find_by_id('id_username').first.fill(self.username)
        self.browser.find_by_id('id_password').first.fill(self.password)
        self.browser.find_by_value('Acessar').first.click()
    
    def loginFalhar(self, url_create):
        """
        :type url_create: String
        """
        self.browser.visit(self.live_server_url + url_create)
        self.browser.find_by_id('id_username').first.fill('wrong_username')
        self.browser.find_by_id('id_password').first.fill(self.password)
        self.browser.find_by_value('Acessar').first.click()

    def logout(self):
        self.browser.visit(self.live_server_url + "/admin/logout/")

class AdminTestCase(ExemploViewsCaseTests):
    ADD_URL = '/admin/'
    
    def test_deveFalhar_loginIncorreto(self):        
        self.loginFalhar(self.ADD_URL)
        self.browser.find_by_value('Log in').first.click()
        assert self.browser.is_element_present_by_text(
            'Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.'
            ) is True