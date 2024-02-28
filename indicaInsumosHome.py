import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import  validate_chain_text_xpaht, validate_text
from loginhelper import LoginHelper
from startSession import StartSession


class IndicaInsumosHome(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test__indicators_home(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("484")

       
      

        
     ##validar titulos de los indicadores 
       
        titlle_value1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/p"
        value_expected1 = ["Indicadores de Insumos (correspondiente a los últimos  6 meses)","Indicadores de Insumos (correspondiente a los últimos  12 meses)"]
        validate_chain_text_xpaht(self.driver, titlle_value1, value_expected1)
     
        titlle_value2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div/swiper/div/div[1]/div[1]/app-supplies-indicator/div/div[1]/div"
        value_expected2 = "Insumos Pendientes de Retirar"
        validate_text(self.driver, titlle_value2, value_expected2)
        
     
    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(IndicaInsumosHome)
  runner = xmlrunner.XMLTestRunner(output='reportIndicaInsumosHome')
  runner.run(test_suite)
        
   
