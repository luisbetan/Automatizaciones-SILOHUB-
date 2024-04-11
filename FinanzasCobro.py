from telnetlib import EC
import unittest
import xmlrunner
import time
from Elements import   delete_element, displace_element_selector, find_elements, find_send_element
from Loginhelper import LoginHelper
from startSession import StartSession




class finanzas_cobro(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_helper = LoginHelper(self.driver)
   
   
    def test_finance_payment(self):
        # Utilizar métodos de LoginHelper para el inicio de sesión
        self.login_helper.login("admingd@silohub.ag", "G@viglio123")
        self.login_helper.select_tenant()
        self.login_helper.search_and_select_account("484")

        select_finance = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[7]/a/span"
        find_elements(self.driver,select_finance)
        time.sleep(2)

        select_payment = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[7]/div/ul/li[1]/a"
        find_elements(self.driver,select_payment)
        time.sleep(2)

        # seleccionar primer movimiento del listado 

        select_liq_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-charges/app-responsive-table/div/div/table/tbody/tr/th/input"
        find_elements(self.driver, select_liq_list)
        time.sleep(2)

        select_button_charge = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-charges/div[1]/div[2]/div/button"
        find_elements(self.driver,select_button_charge)
        time.sleep(2)

        select_edit_amount = "#layout-wrapper > div > div > div > app-forecast-main > div > app-selected-voucher > app-responsive-table > div > div.table-responsive > table > tbody > tr > td:nth-child(5) > app-row-for-finance-forecast > td > div > svg-icon:nth-child(2) > svg"
        displace_element_selector(self.driver,select_edit_amount)
        time.sleep(2)

        delete_amount = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-forecast-main/div/app-selected-voucher/app-responsive-table/div/div[2]/table/tbody/tr/td[5]/app-row-for-finance-forecast/td/div/input"
        delete_element(self.driver,delete_amount)
        time.sleep(3)


        insert_amount = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-forecast-main/div/app-selected-voucher/app-responsive-table/div/div[2]/table/tbody/tr/td[5]/app-row-for-finance-forecast/td/div/input"
        send_amount = "10000"
        find_send_element(self.driver, insert_amount, send_amount )
        time.sleep(5)


        accept_edit = "body > div > div > div.swal2-actions > button.swal2-confirm.f-size-14.swal2-styled"
        displace_element_selector(self.driver, accept_edit)
        time.sleep(2)

        accept_edit = "body > div > div > div.swal2-actions > button.swal2-confirm.f-size-14.swal2-styled"
        displace_element_selector(self.driver, accept_edit)
        time.sleep(2)
        
        

        add_payment = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-forecast-main/div/app-means-of-payment-table/div/div/div/app-button/button"
        find_elements(self.driver,add_payment)
        time.sleep(2)

        

    def tearDown(self):
           self.driver.close()


if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(finanzas_cobro)
  runner = xmlrunner.XMLTestRunner(output='reportFinanzasCobros')
  runner.run(test_suite)