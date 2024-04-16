from telnetlib import EC
import unittest
import xmlrunner
import time
from Elements import   find_elements, find_send_element, search_and_displace_account, select_option_click, validate_text
from LoginSample import LoginSample
from startSession import StartSession




class logistica_secundarias(unittest.TestCase):
    
    def setUp(self):
       
       
        self.start_session = StartSession()
        self.driver = self.start_session.driver
        # Inicializar la clase LoginHelper
        self.login_sample = LoginSample(self.driver)
   
   
    def test_logistics_primaries(self):
        # Utilizar métodos de LoginSample para el inicio de sesión
        self.login_sample.login("admingd@silohub.ag", "G@viglio123")
        self.login_sample.select_tenant()
      

        select_logistics= "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[6]/a/span"
        find_elements(self.driver,select_logistics)
        time.sleep(2)

        quota_request = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[2]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[6]/div/ul/li/a"
        find_elements(self.driver, quota_request)
        time.sleep(2)

        select_operations_secondary = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[1]/div[2]/select"
        option_operations_secondary = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[1]/div[2]/select/option[2]"
        select_option_click(self.driver, select_operations_secondary, option_operations_secondary )
        time.sleep(2)

        located_element = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[1]/div/div[1]/div[2]/app-customer-searcher/ng-select/div/div/div[3]/input"
        select_input = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[1]/div/div[1]/div[2]/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        account_number = "1023"
        search_and_displace_account(self.driver, account_number, select_input, located_element )
        time.sleep(2)

        select_account = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[1]/div/div[1]/div[2]/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        find_elements(self.driver,select_account)
        time.sleep(2)


        select_product = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[1]/div/div[2]/div[2]/div/div[1]/select"
        option_product = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[1]/div/div[2]/div[2]/div/div[1]/select/option[20]"
        select_option_click(self.driver, select_product, option_product )
        time.sleep(2)

        select_harvest = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[1]/div/div[2]/div[2]/div/div[2]/select"
        option_harvest = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[1]/div/div[2]/div[2]/div/div[2]/select/option[3]"
        select_option_click(self.driver, select_harvest, option_harvest )
        time.sleep(5)

        select_contract = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[2]/div/div/div[2]/app-contract-searcher-logistic/ng-select/div/div/div[2]/input"
        option_contract = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-header/div/div/div[2]/div/div/div[2]/app-contract-searcher-logistic/ng-select/ng-dropdown-panel/div/div[2]/div/span"
        select_option_click(self.driver, select_contract, option_contract )
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        insert_amount1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-quotas/div/table/tbody/tr[1]/td[2]/input"
        send_amount1 = "5"
        find_send_element(self.driver, insert_amount1, send_amount1 )
        time.sleep(2)
        
        insert_comment1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-quotas/div/table/tbody/tr[1]/td[3]/textarea"
        send_comment1 = "Test0001"
        find_send_element(self.driver, insert_comment1, send_comment1 )
        time.sleep(2)

        insert_amount2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-quotas/div/table/tbody/tr[2]/td[2]/input"
        send_amount2 = "3"
        find_send_element(self.driver, insert_amount2, send_amount2 )
        time.sleep(2)

        insert_comment2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-quotas/div/table/tbody/tr[2]/td[3]/textarea"
        send_comment2 = "test0002"
        find_send_element(self.driver, insert_comment2, send_comment2 )
        time.sleep(2)

        insert_amount3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-quotas/div/table/tbody/tr[3]/td[2]/input"
        send_amount3 = "8"
        find_send_element(self.driver, insert_amount3, send_amount3 )
        time.sleep(2)

        insert_comment3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/app-reservation-request-quotas/div/table/tbody/tr[3]/td[3]/textarea"
        send_comment3 = "test0003"
        find_send_element(self.driver, insert_comment3, send_comment3 )
        time.sleep(2)

        select_confirm = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[1]/app-reservation-request/div[2]/div/button[2]"
        find_elements(self.driver,select_confirm)
        time.sleep(10)

        title_popup = "/html/body/div[8]/div/h2"
        tille_expected = "Tu Solicitud fue enviada al sistema"
        validate_text(self.driver, title_popup, tille_expected )

        select_accept = "/html/body/div[8]/div/div[6]/button[3]"
        find_elements(self.driver,select_accept)
        time.sleep(2)

    def tearDown(self):
           self.driver.close()


if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(logistica_secundarias)
  runner = xmlrunner.XMLTestRunner(output='reportLogistsecundarias')
  runner.run(test_suite)