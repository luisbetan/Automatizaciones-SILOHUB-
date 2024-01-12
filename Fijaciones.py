import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.ui import Select
from Elements import find_elements
from LoginSample import LoginSample


from startSession import StartSession


class Fijaciones_precio(unittest.TestCase):


    def    setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_grain_pipup(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()
        

       

        select_grain = '/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/a/span'
        find_elements(self.driver,select_grain )
        time.sleep(2)



        select_fijaciones = self.driver.find_element(By.XPATH,'/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[3]/div/ul/li[1]/a')
        select_fijaciones.click()


        ## validar que estamos en la solapa fijaciones habilitadas 
        elemento = self.driver.find_element(By.XPATH, '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/ul/li[1]/a')
        valor = elemento.text 
        valor_esperado = "Fijaciones Habilitadas"
        if valor == valor_esperado:
           print("Nos encontramos en la solapa Fijaciones Habilitadas")
        else:
           print("no estamos ubicados en la solapa Fijaciones Habilitadas") 

       ## localiza el input y envia el número de la cuenta 
        input_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/div/div[1]/app-bindings-enabled-list/app-header-for-responsive-table/div/div/div[1]/div/div/app-customer-searcher/ng-select/div/div/div[2]/input")))
        input_element.send_keys('1023')
      
       #selecciona el elemento oculto y crea un botón para hacer click sobre el 
        element_to_click = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/div/div[1]/app-bindings-enabled-list/app-header-for-responsive-table/div/div/div[1]/div/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div/span")))
        self.driver.execute_script("arguments[0].style.display = 'block';", element_to_click)
        element_to_click.click()
        time.sleep(3)
       

        select_button_pinup = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-bindings/div/div[1]/app-bindings-enabled-list/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[5]/div/div[2]/app-button/button")
        select_button_pinup.click()

        ## validar titulo de la pagima 


        title_pinup_grain = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div[1]/div[1]/section/form/div/h2")
        title_pinup_grain_obtained = title_pinup_grain.text
        title_pinup_grain_expected = "Nueva Fijación de Precio"
        if title_pinup_grain_expected == title_pinup_grain_obtained:
           print("El título de la pagina es: ",title_pinup_grain_obtained)
        else:
           print("No se encontro el título de la pagina")

        ## ingresar cantidad a fijar 
        insert_amount_grain = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div[1]/div[1]/section/form/div/div/div[6]/div/div/input")
        insert_amount_grain.send_keys("100")
        insert_amount_grain.send_keys(Keys.ENTER)
        time.sleep(2)

        ## selecciona el mercado 

        select_market = Select(self.driver.find_element(By.CSS_SELECTOR,'select[aria-label="Default select example"]'))
        select_market.select_by_value("ROS") 

        selected_option = select_market.first_selected_option
        selected_option.click()

        ## insertar el precio

        insert_price_grain = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div[1]/div[1]/section/form/div/div/div[12]/div/div/input")
        insert_price_grain.send_keys("30000")
        insert_price_grain.send_keys(Keys.ENTER)
        time.sleep(2)

        ## seleccionar fecha 

        select_date = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div[1]/div[1]/section/form/div/div/div[16]/app-date-picker/div/input[2]")
        select_date.click()
        time.sleep(2)

        select_date_day = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[2]/div/span[37]")
        select_date_day.click()
        time.sleep(2)

        select_nex_button = self.driver.find_element(By.XPATH,"/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-set-price/div[1]/div[1]/section/form/div/div/div[18]/div/div[2]/app-button/button")
        select_nex_button.click()
        time.sleep(2)







    
    def tearDown(self):
        self.driver.quit()







if __name__ == "__main__":
  unittest.main(verbosity= 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'reporte_fijaciones'))
        