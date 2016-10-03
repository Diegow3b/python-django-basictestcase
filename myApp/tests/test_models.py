# -*- coding: utf-8 -*-
from django.test import TestCase
from myApp.models import myModel
from django.core.exceptions import ValidationError

# Create your tests here.
class ExemploCaseTests(TestCase):
    '''
    Uma forma de chamar este teste diretamente:
        python manage.py test myApp.tests.model_tests.ExemploCaseTests
    '''
    # python manage.py test pedido.tests.test_models.ExemploCaseTests
    def setUp(self):
        super(ExemploCaseTests, self).setUp()

    def test_basic_creation(self):
        '''
            Nome: Teste_0001 a myApp/creation
            Objetivo: 
                    Verificar a criação básica do modelo
        '''
        modelo, created = myModel.objects.get_or_create(atributo_string="valor", atributo_int=10)
        self.assertEqual(created, True)
        self.assertEqual(modelo.atributo_string, "valor")
        self.assertEqual(modelo.atributo_int, 10)

    def test_basic_creationDeveFalhar(self):
        '''
            Nome: Teste_0002 a myApp/creation
            Objetivo: 
                    Deve falhar ao tentar inserir no banco com valores não permitidos
        '''
        
        with self.assertRaises(ValueError):
            modelo, created = myModel.objects.get_or_create(atributo_string="valor", atributo_int="valor improprio")

    def test__unicode__(self):
        '''
            Nome: Teste_0003 a myApp/__unicode__
            Objetivo: 
                    Verificar o retorno da representação do objeto
        '''
        modelo, created = myModel.objects.get_or_create(atributo_string="valor", atributo_int=10)
        self.assertEqual(modelo.__unicode__(), modelo.atributo_string)

    def test_getAtributo_string(self):
        '''
            Nome: Teste_0004 a myApp/getAtributo_string
            Objetivo: 
                    Verificar o retorno da função getAtributo_string
        '''
        modelo, created = myModel.objects.get_or_create(atributo_string="valor", atributo_int=10)
        self.assertEqual(modelo.getAtributo_string(), "valor")

    def test_setAtributo_string(self):
        '''
            Nome: Teste_0005 a myApp/setAtributo_string
            Objetivo: 
                    Verificar o funcionamento da função setAtributo_string
        '''
        modelo, created = myModel.objects.get_or_create(atributo_string="valor", atributo_int=10)
        modelo.setAtributo_string("novo_valor")
        self.assertEqual(modelo.atributo_string, "novo_valor")

    def test_divisaoValoresSucesso(self):
        '''
            Nome: Teste_0006 a myApp/divisaoValores
            Objetivo: 
                    Verificar se a função está dividindo os valores passados por 
                    parametro
        '''
        total = myModel.divisaoValores(4,2)
        self.assertEqual(total, 2)

    def test_divisaoValoresDeveFalhar(self):
        '''
            Nome: Teste_0007 a myApp/divisaoValores
            Objetivo: 
                    Verificar se a função está dividindo os valores passados por 
                    parametro
        '''
        
        with self.assertRaises(ValidationError):
            total = myModel.divisaoValores(5,0)

    def test_post_save_myModel(self):
        '''
            Nome: Teste_0008 a myApp/post_save
            Objetivo: 
                    Verificar se a TRIGGER esta alterando o objeto no banco apos
                    ser criado
        '''
        modelo, created = myModel.objects.get_or_create(atributo_string="valor", atributo_int=10, atributo_boolean = False)        
        self.assertEqual(modelo.atributo_boolean, True)