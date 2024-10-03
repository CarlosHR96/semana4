from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class EditarProductoPage():
    def __init__(self,driver) :
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
        
    localizador_campo_codigo=(By.ID,'id_codigo')    
    localizador_nombre_codigo=(By.ID,'id_nombre')  
    localizador_descripcion_codigo=(By.ID,'id_descripcion')  
    localizador_cantidad_minima_codigo=(By.ID,'id_cantidad_minima')  
    localizador_precio_codigo=(By.ID,'id_precio')  
    boton_editar=(By.ID,'btnEdit')

    def abrir(self,url):
        self.driver.get(url)

    def ingresar_codigo(self,codigo):
        try:
           campo_codigo=self.wait.until(EC.element_to_be_clickable(self.localizador_campo_codigo))      
           #campo_codigo=self.driver.find_element(By.ID,"id_inexistente")
           campo_codigo.clear()
           campo_codigo.send_keys(codigo)

        except NoSuchElementException:
            raise Exception("No se pudo recuperar el campo codigo") 
        except TimeoutException: #element_to_be_clickable
            raise Exception("No se pudo recuperar el campo Código o este no se encuentra activo")
        
    
    def ingresar_nombre(self,nombre):
        nombre_codigo=self.wait.until(EC.element_to_be_clickable(self.localizador_nombre_codigo))      
        nombre_codigo.clear()
        nombre_codigo.send_keys(nombre)

        #self. driver.execute_script("document.getElementById('id_nombre').value='radio actualizado';")
        #metodo java script
    
    def ingresar_descripcion(self,descripcion):
        descripcion_codigo=self.wait.until(EC.element_to_be_clickable(self.localizador_descripcion_codigo))      
        descripcion_codigo.clear()
        descripcion_codigo.send_keys(descripcion)
    
    def ingresar_cantidad_minima(self,cantidad_minima):
        cantidad_minima_codigo=self.wait.until(EC.element_to_be_clickable(self.localizador_cantidad_minima_codigo))      
        cantidad_minima_codigo.clear()
        cantidad_minima_codigo.send_keys(cantidad_minima)

    def ingresar_precio(self,precio):
        precio_codigo=self.wait.until(EC.element_to_be_clickable(self.localizador_precio_codigo))      
        precio_codigo.clear()
        precio_codigo.send_keys(precio)
    
    def editar(self):
        self.wait.until(EC.element_to_be_clickable(self.boton_editar)).click()