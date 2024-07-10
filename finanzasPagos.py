import unittest
import xmlrunner
import time
from Elements import find_elements, validate_text
from loginhelper import LoginHelper
from startSession import StartSession




class finanzaspagos(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)
   
   
    def test_finance_payment(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("1023")



        # ingresar al menú de finanza 

        select_menu_finance = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[7]/a/span"
        find_elements(self.driver, select_menu_finance)
        time.sleep(2)

        select_menu_payment = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[7]/div/ul/li[1]/a"
        find_elements(self.driver, select_menu_payment)
        time.sleep(2)

        # validar el título de la pagina 

        title_vouchers = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-charges/div[2]/div/div[1]"
        title_vouchers_expected = "Listado de Comprobantes"
        validate_text(self.driver, title_vouchers, title_vouchers_expected)
        time.sleep(2)

       ## seleccionar el primer movimiento del listado

        select_movements_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-charges/app-responsive-table/div/div/table/tbody/tr[1]/th/input"
        find_elements(self.driver, select_movements_list)
        time.sleep(2)
       
       # selecciona el botón de cobrar
       
        select_button_payment = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-charges/div[1]/div[2]/div/button'
        find_elements(self.driver, select_button_payment)
        time.sleep(2)

       ## editar monto 
        
        select_icon_pencil = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-forecast-main/div/app-selected-voucher/app-responsive-table/div/div[2]/table/tbody/tr/td[5]/app-row-for-finance-forecast/td/div/svg-icon[1]/svg"
        find_elements(self.driver, select_icon_pencil)
        time.sleep(2)

       

    

    def tearDown(self):
        self.driver.close()





if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(finanzaspagos)
  runner = xmlrunner.XMLTestRunner(output='reportfinanzaspago')
  runner.run(test_suite)
        
