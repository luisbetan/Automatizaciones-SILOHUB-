import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_elements, validate_character_numeric_element, validate_image_css_selector, validate_image_xpaht, validate_text
from Loginhelper import LoginHelper
from startSession import StartSession


class HomeResNegocioTenant(unittest.TestCase):
   def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

   def test_start_tenant(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")
        time.sleep(6)

        
       ## validar si el texto es visible para el usuario 
        page_hello = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/app-welcome-home/div/div[1]/div/p'
        text_expected = "Buen día JUAN DEMO!"
        validate_text(self.driver, page_hello, text_expected  )

        self.driver.execute_script("window.scrollTo(0,200);")
        time.sleep(2)

      ## Seleccionar el elemento que contiene el texto 

        element5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[1]/div[1]/div/p"
        text_expected = "Resumen de Mis Negocios de Granos"
        validate_text(self.driver,element5 , text_expected)

        

        # Seleccionar el elemento de la imagen
        
        image_1 = 'img[src="assets/images/grains/soja.svg"]'
        image_1_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
        validate_image_css_selector(self.driver, image_1, image_1_expected)

        # Seleccionar el elemento de la imagen

        image_2 = 'img[src="assets/images/grains/maiz.svg"]'
        image_2_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
        validate_image_css_selector(self.driver, image_2, image_2_expected)

        # Seleccionar el elemento de la imagen
        
        image_3 = 'img[src="assets/images/grains/trigo.svg"]'
        image_3_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
        validate_image_css_selector(self.driver, image_3, image_3_expected)

        

        ## validar los campor del resumen de mis negocios 
    
       ## entregado
       
        element6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[2]/app-indicator-card/div/div[2]/div[1]/div[2]"
        validate_character_numeric_element(self.driver, element6  )
        time.sleep(2)
        ## fijado 

        element7 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[3]/app-indicator-card/div/div[2]/div[1]/div[2]'
        validate_character_numeric_element(self.driver, element7  )
        time.sleep(2)
         ## pesificado

        element8 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[4]/app-indicator-card/div/div[2]/div[1]/div[2]'
        validate_character_numeric_element(self.driver, element8  )
        time.sleep(2)
        ## liquidado

        element9 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[5]/app-indicator-card/div/div[2]/div[1]/div[2]'
        validate_character_numeric_element(self.driver, element9  )
        time.sleep(2)
          ## pagado

        element10 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[6]/app-indicator-card/div/div[2]/div[1]/div[2]'
        validate_character_numeric_element(self.driver, element10  )
        time.sleep(2)
        
        
        
   def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(HomeResNegocioTenant)
  runner = xmlrunner.XMLTestRunner(output='reportHomeResNegocioTenat')
  runner.run(test_suite)
        
   

        
   
