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
        # executable_path = {'executable_path':'/usr/bin/google-chrome'}
        # executable_path = {'executable_path':'/home/diego/Documents/faculdade/projeto-teste/vm/bin/chromedriver'}
        # cls.browser = Browser('chrome', **executable_path)
        cls.browser = Browser('chrome')
        # cls.browser = Browser('phantomjs')
        # cls.browser.driver.maximize_window()

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
        self.browser.find_by_value('Log in').first.click()
    
    def loginFalhar(self, url_create):
        """
        :type url_create: String
        """
        self.browser.visit(self.live_server_url + url_create)
        self.browser.find_by_id('id_username').first.fill('wrong_username')
        self.browser.find_by_id('id_password').first.fill(self.password)
        self.browser.find_by_value('Log in').first.click()

    def logout(self):
        self.browser.visit(self.live_server_url + "/admin/logout/")

class AdminTestCase(ExemploViewsCaseTests):
    ADD_URL = '/admin/'


    # def test_devePassar_login(self): 
    #     # self.logout()       
    #     self.login(self.ADD_URL)
    #     assert self.browser.is_element_present_by_text(
    #         'AUTHENTICATION AND AUTHORIZATION'
    #         )
    
    def test_deveFalhar_loginIncorreto(self):          
        self.loginFalhar(self.ADD_URL)        
        self.assertTrue(self.browser.is_text_present('Please enter the correct username'))        

    def test_devePassar_inserirModelo(self):
        self.ADD_URL = '/admin/myApp/mymodel/add/'
        self.login(self.ADD_URL)
        self.browser.find_by_id('id_atributo_string').first.fill('kaka')
        self.browser.find_by_name('_save').first.click()
        self.assertTrue(self.browser.is_text_present('added successfully.'))

    def test_deveFalhar_inserirModelo(self):
        self.ADD_URL = '/admin/myApp/mymodel/add/'
        self.login(self.ADD_URL)
        self.browser.find_by_name('_save').first.click()
        self.assertTrue(self.browser.is_text_present('This field is required.'))

    def test_deveFalhar_invalidTypeAttribute(self):
        self.ADD_URL = '/admin/myApp/mymodel/add/'
        self.login(self.ADD_URL)
        self.browser.find_by_id('id_atributo_int').first.fill('typing string on int field')
        self.browser.find_by_name('_save').first.click()
        self.assertTrue(self.browser.is_text_present('Enter a whole number.'))

    def test_devePassar_deleteData(self):
        self.ADD_URL = '/admin/myApp/mymodel/add/'
        self.login(self.ADD_URL)
        self.browser.find_by_id('id_atributo_string').first.fill('teste')
        self.browser.find_by_id('id_atributo_int').first.fill(1)
        self.browser.find_by_name('_save').first.click()
        self.browser.find_by_id('action-toggle').first.check()
        self.browser.find_by_name('action').first.select('delete_selected')
        self.browser.find_by_name('index').first.click()
        self.browser.find_by_value("Yes, I'm sure").first.click()
        self.assertTrue(self.browser.is_text_present('Successfully deleted'))

    def test_devePassar_editExistingData(self):
        self.ADD_URL = '/admin/myApp/mymodel/add/'
        self.login(self.ADD_URL)
        self.browser.find_by_id('id_atributo_string').first.fill('teste')
        self.browser.find_by_id('id_atributo_int').first.fill(1)
        self.browser.find_by_name('_save').first.click()
        self.assertTrue(self.browser.is_text_present('teste', wait_time=2))
        self.browser.find_by_xpath(xpath='//th[@class="field-atributo_string"]//a').first.click()        
        self.browser.find_by_id('id_atributo_string').first.fill('modified')
        self.browser.find_by_id('id_atributo_int').first.fill(999)
        self.browser.find_by_name('_save').first.click()
        self.assertTrue(self.browser.is_text_present('modified'))