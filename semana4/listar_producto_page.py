from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ListarProductoPage():
    def __init__(self,driver) :
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
        
    localizador_campo_codigo=(By.ID,'id_codigo') 
    localizador_boton_buscar=(By.XPATH,"//button[contains(@class, 'btn') and contains(@class, 'bg-black')]")
    boton_ver=(By.ID,"view_record") 
    localizador_primera_fila=(By.CSS_SELECTOR,"#datatable > tbody > tr:first-child") 
 

    def abrir(self,url):
        self.driver.get(url)

    def ingresar_codigo_a_buscar(self,codigo):
        campo_codigo=self.wait.until(EC.element_to_be_clickable(self.localizador_campo_codigo))      
        campo_codigo.clear()
        campo_codigo.send_keys(codigo)

    def buscar(self):
        self.wait.until(EC.element_to_be_clickable(self.localizador_boton_buscar)).click()
      
    def seleccionar_primera_fila(self):
        primera_fila=self.wait.until(EC.element_to_be_clickable(self.localizador_primera_fila))  
        actions=ActionChains(self.driver)
        actions.move_to_element(primera_fila).click().perform()


    def ver(self):
 
        self.wait.until(EC.element_to_be_clickable(self.boton_ver)).click()
  