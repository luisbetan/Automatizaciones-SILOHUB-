import time
import unittest
from selenium.webdriver.common.by import By
import xmlrunner
from Elements import find_and_click_element_selector, find_elements, validate_character_numeric_element, validate_text
from loginhelper import LoginHelper
from startSession import StartSession


class Metricas(unittest.TestCase):
    def setUp(self):
        self.start_session = StartSession()
        self.driver = self.start_session.driver

        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)

    def test_metricas(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")

        ##seleccionar el botón filtro 
        select_menu_metrics = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[9]/a/span"
        find_elements(self.driver, select_menu_metrics)
      

        ## validar el titulo 
        title_page = '/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span'
        text_expected = "MÉTRICAS"
        validate_text(self.driver, title_page, text_expected  )
 
        ## seleccionar filtro 01/01/2024 al 15/03/2024

        select_filter = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/div/div/app-date-picker/div/input[2]"
        find_elements(self.driver, select_filter)
     
        select_arrow_1 = "body > div > div.flatpickr-months > span.flatpickr-prev-month"
        clicks = 2
        find_and_click_element_selector(self.driver, select_arrow_1, clicks)
        time.sleep(2)

        select_date1 = "/html/body/div/div[2]/div/div[2]/div/span[1]"
        find_elements(self.driver, select_date1)

        select_arrow_2 = "body > div > div.flatpickr-months > span.flatpickr-next-month"
        clicks = 2
        find_and_click_element_selector(self.driver, select_arrow_2, clicks)
        time.sleep(2)
        
        select_date2 = "/html/body/div/div[2]/div/div[2]/div/span[19]"
        find_elements(self.driver, select_date2)


        
     ##validar los cuadrantes de la pantalla verificando los que vienen de la base de datos si son caracteres numericos 
        
        element1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[1]/app-metric-indicator/div/div[2]/div[2]'
        validate_character_numeric_element(self.driver, element1  )
       
        titlle_value1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[1]/app-metric-indicator/div/div[2]/div[3]"
        value_expected1 = "Total Cuentas ERP"
        validate_text(self.driver, titlle_value1, value_expected1)
     
   
        element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[2]/app-metric-indicator/div/div[2]/div[2]'
        validate_character_numeric_element(self.driver, element2  )

        ##validar totalizadores  a vencer
        titlle_value2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[2]/app-metric-indicator/div/div[2]/div[3]"
        value_expected2 = "Total Cuentas Vinculadas"
        validate_text(self.driver, titlle_value2, value_expected2)

        element3 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[3]/app-metric-indicator/div/div[2]/div[2]'
        validate_character_numeric_element(self.driver, element3  )
        
        titlle_value3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[3]/app-metric-indicator/div/div[2]/div[3]"
        value_expected3 = "Cuentas Pend. de Vincular"
        validate_text(self.driver,titlle_value3, value_expected3)

        
        element4 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[4]/app-metric-indicator/div/div[2]/div[2]'
        validate_character_numeric_element(self.driver, element4  )

        titlle_value4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[4]/app-metric-indicator/div/div[2]/div[3]"
        value_expected4 = "Porc. Vinculado"
        validate_text(self.driver, titlle_value4, value_expected4)



       
         ## validar cuadrantes que vienen desde google analitycs
        
        element5 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[5]/app-metric-indicator-news-clients/app-metric-indicator/div/div[3]/div[2]'
        validate_character_numeric_element(self.driver, element5  )

        titlle_value5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[5]/app-metric-indicator-news-clients/app-metric-indicator/div/div[3]/div[3]"
        text_expected = "Productores Nuevos"
        validate_text(self.driver,titlle_value5 , text_expected)

        element6 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[6]/app-metric-indicator-total-logins/app-metric-indicator/div/div[3]/div[2]'
        validate_character_numeric_element(self.driver, element6  )

        titlle_value6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[6]/app-metric-indicator-total-logins/app-metric-indicator/div/div[3]/div[3]"
        text_expected = "Total Logins (Visitas)"
        validate_text(self.driver,titlle_value6 , text_expected)

        element7 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[7]/app-metric-indicator-unique-logins/app-metric-indicator/div/div[3]/div[2]'
        validate_character_numeric_element(self.driver, element7  )

        titlle_value7 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[7]/app-metric-indicator-unique-logins/app-metric-indicator/div/div[3]/div[3]"
        text_expected = "Usuarios Logueados"
        validate_text(self.driver,titlle_value7 , text_expected)

        element8 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[8]/app-metric-indicator-session-avg/app-metric-indicator/div/div[3]/div[2]'
        validate_character_numeric_element(self.driver, element8  )

        titlle_value8 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-metric/app-metric-swiper-indicators/div/swiper/div/div[1]/div[8]/app-metric-indicator-session-avg/app-metric-indicator/div/div[3]/div[3]"
        text_expected = "Tiempo Prom. Sesión"
        validate_text(self.driver,titlle_value8 , text_expected)




       
    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(Metricas)
  runner = xmlrunner.XMLTestRunner(output='reportMetricas')
  runner.run(test_suite)
        
   