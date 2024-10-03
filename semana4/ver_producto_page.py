    
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VerProductoPage():
    def __init__(self,driver) :
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    
    
    localizador_campo_codigo=(By.XPATH,'//*[@id="datatable"]/tbody/tr[1]/td[2]')    
    localizador_nombre_codigo=(By.XPATH,'//*[@id="datatable"]/tbody/tr[2]/td[2]')  
    localizador_descripcion_codigo=(By.XPATH,'//*[@id="datatable"]/tbody/tr[3]/td[2]')  
    localizador_cantidad_minima_codigo=(By.XPATH,'//*[@id="datatable"]/tbody/tr[5]/td[2]')  
    localizador_precio_codigo=(By.XPATH,'//*[@id="datatable"]/tbody/tr[4]/td[2]')  
    localizador_titulo_formulario=(By.CSS_SELECTOR,'.card-title')



    def abrir(self,url):
        self.driver.get(url)

    def recuperar_codigo(self):
        campo_codigo=self.wait.until(EC.visibility_of_element_located(self.localizador_campo_codigo)) 
        return campo_codigo.text   
      
    def recuperar_nombre(self):
        campo_nombre=self.wait.until(EC.visibility_of_element_located(self.localizador_nombre_codigo)) 
        return campo_nombre.text  
    
    def recuperar_descripcion(self):
        campo_descripcion=self.wait.until(EC.visibility_of_element_located(self.localizador_descripcion_codigo)) 
        return campo_descripcion.text  

    def recuperar_cantidad_minima(self):
        campo_cantidad_minima=self.wait.until(EC.visibility_of_element_located(self.localizador_cantidad_minima_codigo)) 
        return campo_cantidad_minima.text 

    def recuperar_precio(self):
        campo_precio=self.wait.until(EC.visibility_of_element_located(self.localizador_precio_codigo)) 
        return campo_precio.text            
 
    def recuperar_titulo(self):
        campo_titulo=self.wait.until(EC.visibility_of_element_located(self.localizador_titulo_formulario)) 
        return campo_titulo.text
     

