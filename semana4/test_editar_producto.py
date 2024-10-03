
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import HtmlTestRunner
from editar_producto_page import EditarProductoPage
from listar_producto_page import ListarProductoPage
from ver_producto_page import VerProductoPage
import os
import sys
import django
# Agregar la ruta del directorio del proyecto Django al PYTHONPATH
sys.path.append(r"C:\clase4\proyecto\miproyecto")
# Configurar la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miproyecto.settings')
# Inicializar Django
django.setup()
from producto.models import Producto

class EditarProductoTest (unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        cls.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.url_base='http://localhost:9000/productos/'
        cls.EditarPage=EditarProductoPage(cls.driver)
        cls.ListarPage=ListarProductoPage(cls.driver)
        cls.VerPage=VerProductoPage(cls.driver)
        Producto.objects.all().delete()
        nuevo_producto=Producto(codigo='00000011',nombre='radio',descripcion='radio fm',precio=20, cantidad_minima=3)
        nuevo_producto.save()
        cls.producto_inicial=Producto.objects.get(codigo='00000011')

    def setUp(self) :
        self.EditarPage.abrir(f"{self.url_base}editar/{self.producto_inicial.id}")
    
    def test_editar_producto(self):
        try:
            pagina_editar= self.EditarPage
            pagina_listar=self.ListarPage
            pagina_ver=self.VerPage
            codigo_producto='0000012'
            nombre_producto='radio actualizado'
            descripcion_producto='radio fm actualizado'
            precio_producto= 30
            cantidad_minima_producto= 5

            pagina_editar.ingresar_codigo(codigo_producto)
            pagina_editar.ingresar_nombre(nombre_producto)
            pagina_editar.ingresar_descripcion(descripcion_producto)
            pagina_editar.ingresar_precio(precio_producto)
            pagina_editar.ingresar_cantidad_minima(cantidad_minima_producto)
            pagina_editar.editar()

            length_codigo=len(codigo_producto)

            self.assertEqual(length_codigo,8, f"El codigo enviado posee {length_codigo} caracteres ")
           
            pagina_listar.ingresar_codigo_a_buscar(codigo_producto)
            pagina_listar.buscar()
            pagina_listar.seleccionar_primera_fila()
            pagina_listar.ver()
        
            codigo_recuperado=pagina_ver.recuperar_codigo()
            nombre_recuperado=pagina_ver.recuperar_nombre()
            descripcion_recuperado=pagina_ver.recuperar_descripcion()
            cantidad_recuperado=pagina_ver.recuperar_cantidad_minima()
            precio_recuperado=pagina_ver.recuperar_precio()
            titulo_recuperado=pagina_ver.recuperar_titulo()
          

            titulo_esperado=f"ID : {self.producto_inicial.id}"
            self.assertEqual(titulo_recuperado,titulo_esperado,"Titulo no coincide con lo esperado")
            self.assertEqual(codigo_recuperado,codigo_producto,"Codigo no coincide con lo esperado")
            self.assertEqual(nombre_recuperado,nombre_producto,"Nombre no coincide con lo esperado")
            self.assertEqual(descripcion_recuperado,descripcion_producto,"Descripcion no coincide con lo esperado")
            self.assertEqual(int(cantidad_recuperado),int(cantidad_minima_producto),"Cantidad no coincide con lo esperado")
            self.assertEqual(float(precio_recuperado),float(precio_producto),"Precio no coincide con lo esperado")
         
        except Exception as e:
            self.fail(str(e))

    @classmethod
    def tearDownClass(cls) :
        Producto.objects.all().delete()
     
        if cls.driver:
            cls.driver.quit()
      


def suite():
    suite = unittest.TestSuite()
    loader=unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(EditarProductoTest))

    return suite

if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(
        output="reportes",
        report_name="actualizar_producto",
        report_title='Actualizar producto previamente creado usando Selenium',
        combine_reports=True,
        add_timestamp=True
    )
    runner.run(suite())




      
    




