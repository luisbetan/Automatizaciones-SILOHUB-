from telnetlib import EC
import unittest
import xmlrunner
import time
from Elements import   find_elements, find_elements_css_selector, find_elements_id, find_send_element, search_and_displace_account, select_option_click, validate_character_numeric_element, validate_text
from LoginSample import LoginSample
from startSession import StartSession




class logistica_MisSolitudes(unittest.TestCase):
    
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

        select_my_request = "current-account-file-tab"
        find_elements_id(self.driver,select_my_request)
        time.sleep(2)

        located_element = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/app-header-for-responsive-table/div/div/div[1]/div/div/app-customer-searcher/ng-select/div/div/div[2]/input"
        select_input = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/app-header-for-responsive-table/div/div/div[1]/div/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        account_number = "1023"
        search_and_displace_account(self.driver, account_number, select_input, located_element )
        time.sleep(2)

        select_account = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/app-header-for-responsive-table/div/div/div[1]/div/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
        find_elements(self.driver,select_account)
        time.sleep(5)

        title_column1 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/thead/tr/th[7]"
        tille_expected = "Estado de Solicitudes"
        validate_text(self.driver, title_column1, tille_expected )

        title_request = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[1]/td[7]/div/div[1]"
        tille_expected = "Solicita-dos"
        validate_text(self.driver, title_request, tille_expected )

        amount_request = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[2]/td[7]/div/div[1]"
        validate_character_numeric_element(self.driver,amount_request)

        title_pending = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[1]/td[7]/div/div[2]"
        tille_expected = "Pen-dientes"
        validate_text(self.driver, title_pending, tille_expected )

        amount_pending = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[2]/td[7]/div/div[2]"
        validate_character_numeric_element(self.driver,amount_pending)

        title_rejected = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[1]/td[7]/div/div[3]"
        tille_expected = "Recha-zados"
        validate_text(self.driver, title_rejected, tille_expected )

        amount_rejected = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[2]/td[7]/div/div[3]"
        validate_character_numeric_element(self.driver,amount_rejected)

        title_received = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[1]/td[7]/div/div[4]"
        tille_expected = "Recibi-dos"
        validate_text(self.driver, title_received, tille_expected )

        amount_received = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[2]/td[7]/div/div[4]"
        validate_character_numeric_element(self.driver, amount_received)



        title_column2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/thead/tr/th[8]"
        tille_expected = "Estado Cupos Asignados"
        validate_text(self.driver, title_column2, tille_expected )


        title_withoutCTG = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[1]/td[8]/div/div[1]"
        tille_expected = "Sin CTG"
        validate_text(self.driver, title_withoutCTG, tille_expected )

        amount_withoutCTG = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[2]/td[8]/div/div[1]"
        validate_character_numeric_element(self.driver,amount_withoutCTG)

        title_CTG = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[1]/td[8]/div/div[2]"
        tille_expected = "CTG"
        validate_text(self.driver, title_CTG, tille_expected )

        amount_CTG = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[2]/td[8]/div/div[4]"
        validate_character_numeric_element(self.driver, amount_CTG)

        title_inDeveloping = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[1]/td[8]/div/div[3]"
        tille_expected = "En Destino"
        validate_text(self.driver, title_inDeveloping, tille_expected )

        amount_Developing = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[2]/td[8]/div/div[3]"
        validate_character_numeric_element(self.driver,amount_Developing)

        title_downloaded = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[1]/td[8]/div/div[4]"
        tille_expected = "Descar-gados"
        validate_text(self.driver, title_downloaded, tille_expected )

        amount_downloaded = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-logistics/div/div[2]/div[2]/app-my-reservations/div/table/tbody/tr[2]/td[8]/div/div[4]"
        validate_character_numeric_element(self.driver, amount_downloaded)

        select_edit = "#current-account-file > app-my-reservations > div > table > tbody > tr:nth-child(2) > td:nth-child(9) > div > svg-icon > svg"
        find_elements_css_selector(self.driver,select_edit)
        time.sleep(5)

        insert_amount = "/html/body/ngb-modal-window/div/div/app-my-request-edit-modal/div[2]/app-my-request-edit-form/div[7]/div[2]/div/div/input"
        send_amount = "1"
        find_send_element(self.driver, insert_amount, send_amount )
        time.sleep(5)

        select_button_save  = "/html/body/ngb-modal-window/div/div/app-my-request-edit-modal/div[2]/app-my-request-edit-form/div[8]/app-button[2]/button"
        find_elements(self.driver,select_button_save)
        time.sleep(5)

        select_button_confirm  = "/html/body/div[8]/div/div[6]/button[3]"
        find_elements(self.driver,select_button_confirm)
        time.sleep(5)

        select_button_accept  = "/html/body/div[8]/div/div[6]/button[1]"
        find_elements(self.driver,select_button_accept)
        time.sleep(5)



    def tearDown(self):
           self.driver.close()


if __name__ == "__main__":
  test_suite = unittest.TestLoader().loadTestsFromTestCase(logistica_MisSolitudes)
  runner = xmlrunner.XMLTestRunner(output='reportLogistMisSolicitud')
  runner.run(test_suite)